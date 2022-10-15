import sqlite3

db = sqlite3.connect('ingridients.db')
cursor = db.cursor()


def get_all_matching(calories, type, taste, vitamin):
    first_data = cursor.execute(f"""SELECT * FROM ingr""").fetchall()
    first_data = [i for i in first_data if type in i[5]]
    if len(first_data) == 0:
        return 'Извините, мы не смогли ничего приготовить по вашему запросу'
    first_data = [i for i in first_data if taste in i[-1]]
    end_data = []
    if vitamin:
        vitamins_data = cursor.execute(f"""SELECT * FROM ingr""").fetchall()
        vitamins_data = [i for i in vitamins_data if vitamin in i[2]]
        for i in vitamins_data:
            if i in first_data:
                end_data.append(i)
    else:
        end_data = first_data
    if len(end_data) == 0:
        return 'Извините, мы не смогли ничего приготовить по вашему запросу'
    calories_for_ingr = calories/len(end_data)
    final = []
    end_data.sort(key=lambda x: x[4])

    for i in end_data:
        final.append(f'{i[1]} {round(calories_for_ingr/i[4] * 100, 2)}гр.')
    if len(final) == 0:
        return 'Извините, мы не смогли ничего приготовить по вашему запросу'
    return final


