def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.
    if context.readDataFile('collective.easyslideshow_various.txt') is None:
        return

    # Add additional setup code here
    """Make the slideshow_folder_view available"""
    portal = context.getSite()
    pt = portal.portal_types
    if  "slideshow_folder_view" not in pt['Folder'].view_methods:
        pt['Folder'].view_methods += ("slideshow_folder_view",)

