from pyscript import display, document

def general_weighted_average(e):
    first = document.getElementById('first_name').value
    last = document.getElementById('last_name').value
    science = float(document.getElementById('science').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    math = float(document.getElementById('math').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)
    #turns string into float
    summary_html = f"""
    Science: {science} | 
    English: {english} | 
    Math: {math} | 
    ICT: {ict} | 
    PE: {pe} | 
    Filipino: {filipino}
    """
    #grades
    units_subject = (5, 3, 2, 1)
    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units
    display(f"Student Name: {first} {last}", target="student_info",)
    #displays student info
    display(summary_html, target="summary", append=False)
    #display the summmary of ur grades
    display(f'Your general weighted average is {gwa:.2f}', target='output')
    #displays the final general weighted average
    

