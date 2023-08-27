def main():

    m_stud = int(input('Enter number of male students: '))
    f_stud = int(input('Enter number of female students: '))

    total = (m_stud + f_stud)

    m_perc = (m_stud / total) * 100
    f_perc = (f_stud / total) * 100

    print(f"Total Numbers of Students: \t {total}")
    print(f"Number of Male & Female Students: \t {m_stud} \t {f_stud}")
    print(f"Percentage of Male & Female Students: \t {m_perc: .2f}% \t {f_perc: .2f}%")


    return m_perc, f_perc


if __name__ == '__main__':
    main()
