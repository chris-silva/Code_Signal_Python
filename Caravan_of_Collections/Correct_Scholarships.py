def correctScholarships(bestStudents, scholarships, allStudents):
    return True if (len(set(bestStudents)-set(scholarships)) == 0) and (len(set(scholarships) - set(allStudents)) == 0) and ( len(set(allStudents) - set(scholarships) ) != 0 ) else False
