async def checkBoxes(page):
      ##################check boxes#####################
    # Select all checkboxes
    await page.wait_for_selector('th:has-text("Classroom Accommodations")')

    checkboxes = await page.query_selector_all('input.READONLYCHECKBOX[type="checkbox"]')
    
    # Check all checkboxes
    for checkbox in checkboxes:
        # Ensuring the checkbox is not already checked to avoid the alert
        is_checked = await checkbox.is_checked()
        if not is_checked:
            await page.evaluate('(checkbox) => checkbox.checked = true', checkbox)
        
    # # headers = await page.query_selector_all('thead th')
    # # ela_index = None
    # # for index, header in enumerate(headers):
    # #     if await header.inner_text() == 'ELA':
    # #         ela_index = index
    # #         break
    
    # # # Ensure that ELA column is found
    # # if ela_index is not None:
    # #     # Check all checkboxes in the ELA column
    # #     checkboxes = await page.query_selector_all(f'tbody tr td:nth-child({ela_index + 1}) input[type="checkbox"]')
    # #     for checkbox in checkboxes:
    # #         await checkbox.check()
    #  # This selector is based on the provided CSS path
    # ela_header_selector = '#DOCCONTENT > div > div > rotate > table > thead > tr > th:nth-child(2) > div > span'
    
    # # Wait for the ELA header to be loaded
    # await page.wait_for_selector(ela_header_selector)
    
    # # Check all checkboxes in the ELA column
    # # Assuming each row in tbody has a checkbox in the same column (2nd column)
    # checkboxes = await page.query_selector_all('#DOCCONTENT > div > div > rotate > table > tbody > tr > td:nth-child(2) > input[type="checkbox"]')
    
    # for checkbox in checkboxes:
    #     await checkbox.check()