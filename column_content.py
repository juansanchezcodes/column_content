'''Returns the contents of a column from a list of lists without displaying duplicates'''
def column_content(a_list_of_lists, column_number):
    contents = []
    for row in a_list_of_lists: 
        content = row[column_number]
        if content not in contents:
            contents.append(content)
            contents.sort(reverse=False)
    return(contents)