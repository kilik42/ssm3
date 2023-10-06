import asyncio
from playwright.async_api import async_playwright
# from checkBox import checkBoxes  # Ensure this is a correct import
import tkinter as tk
from tkinter import ttk
from checkBox import checkBoxes


# Decorator to handle exceptions
def catch_exceptions(toplevel):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(f"Error: {str(e)}")
                # Optionally: Add a message to the GUI about the error
                # toplevel.label_error.config(text=f"Error: {str(e)}")
        return wrapper
    return decorator


async def run_script(first_name, last_name):
    async def run():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto('https://ssm.cps.k12.il.us/userlogin.aspx?WorkspaceID=CPS')
            # (The rest of your playwright code...)

            # Add the checkBoxes function or ensure it's correctly imported and utilized
            # await checkBoxes(page)
            # Use appropriate selectors for your actions. Below are placeholders,
            # you might need to inspect HTML and update these.
            await page.click('"User ID"') # Replace with actual selector for User ID
            await page.fill('"User ID"', 'MAEvins') # Replace with actual user ID
            await page.click('"Password"') # Replace with actual selector for Password
            await page.fill('"Password"', 'Harkonen2383') # Replace with actual password

            # Continue to navigate the website.
            # Replace the selector strings below with the actual ones from the web page.
            await page.select_option('"Log in to"', 'INSTR')
            await page.click('#btnSignIn')
            await asyncio.sleep(1)
            await page.hover('.rmMainMenuImage')
            await page.wait_for_selector('.rmMainMenuText')
            await asyncio.sleep(1)
            await page.click('"Students"')
            await page.click('"Last Name"')
            await page.fill('"Last Name"', last_name)
            await page.click('"First Name"') # Ensure this is a valid selector
            await page.fill('"First Name"', first_name)
            await page.click('#ctl00_TNPageContent_btnQuickSearch_Custom_input')
            await asyncio.sleep(1)
            # await page.click('"Documents"')
            await page.click('img[alt="Documents"]')

            await asyncio.sleep(2)
        
            ######choose 504  plan or other text #########
            await page.click('text=504 Plan >> nth=4')
            # Define all potential text options that might be present on the page
            # possible_texts = ["504 Plan", "Alternative Text 1", "Alternative Text 2"]

            # # Try to click on the text if it exists
            # for text in possible_texts:
            #     try:
            #         await page.click(f'text={text}')
            #         # If successful break the loop as we have found and clicked the text
            #         break
            #     except Exception as e:
            #         print(f"Failed to click on text '{text}': {str(e)}")
            #         # If failed, continue the loop to try the next option

            #####################################clicking academic support########
            # rtbItem rtbTemplate  rtbItemFocused rtbItemHovered
            await asyncio.sleep(1)
            ## academic support section#####
            await page.click('.rtbIcon')
            # await page.wait_for_selector('.rtbItem rtbTemplate  rtbItemFocused rtbItemHovered')
            await asyncio.sleep(1)
            # await page.click('"Search >"')
            # await page.click('"Last Name"')
            # await page.fill('"Last Name"', 'Ga')
            
            # await page.click('"Academic Support"')
        
            # Example of waiting for an element with XPath before interacting with it
            xpath_selector = '/html/body/form/div[9]/div[2]/div/div[1]/div/div/div/div/ul/li[2]/table/tbody/tr[3]/td[1]'
            await page.wait_for_selector(f'xpath={xpath_selector}')
            ##########################end academic support section###################################### 
            # Interacting with the element
            await page.click(f'xpath={xpath_selector}')
            
            await checkBoxes(page)
            await asyncio.sleep(8)
            
            await asyncio.sleep(5)
            await page.screenshot(path='screenshot.png')
            await browser.close()
    await run()


def create_app():
    app = tk.Tk()
    app.title("Student Data Entry")

    label_first_name = ttk.Label(app, text="First Name:")
    label_first_name.pack(pady=5, padx=20, side=tk.LEFT)
    entry_first_name = ttk.Entry(app)
    entry_first_name.pack(pady=5, padx=20, side=tk.LEFT)

    label_last_name = ttk.Label(app, text="Last Name:")
    label_last_name.pack(pady=5, padx=20, side=tk.LEFT)
    entry_last_name = ttk.Entry(app)
    entry_last_name.pack(pady=5, padx=20, side=tk.LEFT)

    # Error Message label
    label_error = ttk.Label(app, text="", foreground="red")
    label_error.pack(pady=5, padx=20, side=tk.BOTTOM)

    # Adding toplevel to app object to access it in the decorator
    app.label_error = label_error
    
    @catch_exceptions(app)
    def on_submit():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        asyncio.run(run_script(first_name, last_name))

    button_submit = ttk.Button(app, text="Submit", command=on_submit)
    button_submit.pack(pady=20)
    
    app.mainloop()


if __name__ == "__main__":
    create_app()
