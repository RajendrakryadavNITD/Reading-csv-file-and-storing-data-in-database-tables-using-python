class Queries (object):
    get_last_inserted_id = "select last_insert_id() as id"

    insert_sample_data_info = "insert into excel_sheet_data (excel_id ,databasecategory " \
                              " ,businessname ,address1, address2, locality, town, " \
                              " country ,postcode, area, postcodearea ,postcodesubarea " \
                              " ,lineofbusiness , sicnumeric , sicdiscription ,telephone" \
                              "  ,tps , fax ,fps ,employeesnumeric, premisestype ,title1" \
                              "  ,fname ,sname ,position1 ,email , emailaddress) " \
                              " values (:excel_id ,:databasecategory , :businessname " \
                              " ,:address1, :address2, :locality, :town, :country ," \
                              "  :postcode, :area, :postcodearea , :postcodesubarea " \
                              " , :lineofbusiness , :sicnumeric , :sicdiscription " \
                              " ,:telephone ,:tps , :fax ,:fps ,:employeesnumeric, " \
                              " :premisestype ,:title1 ,:fname ,:sname ,:position1 ," \
                              " :email , :emailaddress) "

    get_excel_sheet_info = "select id, excel_id, databasecategory, businessname, address1, address2, locality, town, country, postcode, area, postcodearea, postcodesubarea, lineofbusiness, sicnumeric, sicdiscription, telephone, tps, fax, fps, employeesnumeric, premisestype, title1, fname, sname, position1, email, emailaddress from excel_sheet_data limit :startlimit, :count"