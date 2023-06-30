def scrape_job_data_by_mapping():
    from bs4 import BeautifulSoup as bs  # HTML 파싱을 위한 라이브러리
    from selenium import webdriver  # 웹 자동화를 위한 라이브러리
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd  # 데이터 처리 및 분석을 위한 라이브러리

    # 직무 코드와 이름을 매핑하는 사전
    job_mapping = {
        # 사무 관리직
        "일반사무직": "45",
        "기획,사업개발,전략기획": "46",
        "마케팅,시장조사": "47",
        "광고,홍보": "48",
        "IR": "152",
        "인사,인재개발": "50",
        "경리,회계,세무,재무,총무": "53",
        "비서": "49",
        "무역,수출입": "51",
        "인허가,인증": "153",
        "구매,자재": "52",
        "기타 사무 관리직 관련": "164",
        "이커머스": "346",
        # 영업직
        "해외영업": "56",
        "기술영업": "57",
        "영업관리": "58",
        "국내영업, 판매세일즈": "59",
        "도매,소매,대리점관리": "60",
        "매장관리,판촉,고객관리": "61",
        "서비스관리": "62",
        "텔레마케팅": "63",
        "바이오,의약,제약": "154",
        "의료기기": "155",
        "기타 영업직 관련": "64",
        # 기술직
        "생산관리,품질관리": "66",
        "건축,토목,시공,설계,인테리어": "67",
        "기계,금속": "68",
        "조선,항공,우주": "69",
        "전기,설비": "70",
        "화학,화공,섬유": "71",
        "환경": "72",
        "광학,사진,인쇄": "73",
        "생명과학,농림": "74",
        "제조,생산": "75",
        "의료기기": "156",
        "기타 기술직 관련": "76",
        # 연구개발
        "전기": "78",
        "기계": "79",
        "전자,반도체": "80",
        "제어": "81",
        "화학,화공,섬유": "82",
        "금속,재료,신소재": "83",
        "유전공학,생명,생물": "84",
        "식품": "85",
        "환경,수질,대기,폐기물": "86",
        "인문,사회과학": "87",
        "바이오,의약,제약": "157",
        "의료기기": "158",
        "기타 연구개발 관련": "88",
        # 서비스, 고객지원, 유통 코드
        "고객지원": "90",
        "스튜디어스, 승무원": "91",
        "호텔,외식": "92",
        "요리,영양사": "93",
        "여행,관광": "94",
        "의류": "95",
        "기타": "96",
        "물류.운송.배송": "97",
        # 전문직
        "컨설팅,MBA": "99",
        "증권.투자분석가": "100",
        "외환,국제금융,펀드매니져": "101",
        "변호사,법률,법무": "102",
        "회계사,세무사,관세사": "103",
        "노무사,직업전문가": "104",
        "감정사,평가사,경매사": "105",
        "특허,변리사": "106",
        "보험계리사,손해사정인": "107",
        "기자,취재,편집,방송,편성": "108",
        "광고기획,제작": "109",
        "디자인": "110",
        "사서,문서관리": "111",
        "출판,편집": "112",
        "번역,통역": "113",
        "사회복지": "114",
        "채권관리": "115",
        "투자,상담,분석,조사": "116",
        "의사,약사,간호사": "117",
        "MSL": "159",
        "부동산,공인중개사": "118",
        "강사,교육": "119",
        "기타": "120",
        # 인터넷
        "웹기획,컨텐츠기획,프로젝트관리": "122",
        "디지털 마케팅": "123",
        "웹프로그래머": "124",
        "웹디자인": "125",
        "전자상거래": "128",
        "UI / UX": "160",
        "빅데이타": "161",
        "인공지능": "162",
        "고객지원,상담,교육": "131",
        "기타": "132",
        "웹마스터": "126",
        "정보검색": "127",
        "인터넷 영업": "129",
        "멀디미디어 자료제작": "130",
        # 정보통신, 전자, 전산
        "컨설팅": "134",
        "프로젝트관리": "135",
        "시스템조사,분석,설계": "136",
        "프로그램개발,유지보수": "137",
        "네트워크관리,컨설팅영업": "138",
        "시스템유통,HW영업": "140",
        "기술지원": "141",
        "전산관련업무": "142",
        "SI 영업,solution 영업": "143",
        "소프트웨어개발": "144",
        "패키지영업,SW영업": "145",
        "전산총괄업무": "146",
        "이동통신": "147",
        "정보통신": "148",
        "마이크로프로세서": "149",
        "기타": "150",
        "패키지개발,제작": "139",
    }

    # 크롬 옵션 지정
    chrome_options = webdriver.ChromeOptions()

    # 드라이버 설정
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    # 직무 목록 출력
    print("직무 목록:")
    for i, job in enumerate(job_mapping, start=1):
        print(f"{i}. {job}")

    # 직무 선택
    selection = int(input("원하는 직무의 번호를 입력해주세요: "))
    if selection < 1 or selection > len(job_mapping):
        print("잘못된 선택입니다.")
    else:
        selected_job = list(job_mapping.keys())[selection - 1]
        print(f"선택한 직무: {selected_job}")

        # 선택한 직무에 대한 추가 작업 수행
        # 예시: 해당 직무의 코드를 가져와서 웹 스크래핑 작업 수행
        job_code = job_mapping.get(selected_job)
        if job_code is None:
            print("해당 직무의 코드를 찾을 수 없습니다.")
        else:
            # 동적으로 변경된 URL로 이동
            driver.get(
                f"https://www.peoplenjob.com/jobs?type=work&work_code_id={job_code}"
            )

            html = driver.page_source
            soup = bs(html, "html.parser")

            # tbody 안의 tr태그 가져옴
            job_soup = soup.select("tbody > tr")

            job_open_list = []
            job_title_list = []
            job_type_list = []
            job_searchfirm_list = []
            job_location_list = []
            job_deadline_list = []

            for job in job_soup:
                job_open = job.find("td", class_="date").text
                job_title = (
                    job.find("td", class_="job-title").text.strip().replace("\n", "")
                )
                job_type = (
                    job.find("td", class_="job_type")
                    .text.strip()
                    .replace("\n", "")
                    .replace(" / ", " ")
                    .replace(".", ", ")
                )
                job_searchfirm = (
                    job.find("td", class_="name").text.strip().replace("\n", "")
                )
                job_location = job.select("td > a")[-1].text.strip().replace("\n", "")
                job_deadline = (
                    job.find("span", class_="job-fin-date")
                    .text.strip()
                    .replace("\n", "")
                )

                job_open_list.append(job_open)
                job_title_list.append(job_title)
                job_type_list.append(job_type)
                job_searchfirm_list.append(job_searchfirm)
                job_location_list.append(job_location)
                job_deadline_list.append(job_deadline)

            # 데이터프레임 생성
        df = pd.DataFrame(
            {
                "채용 시작일": job_open_list,
                "채용 직무 정보": job_title_list,
                "직무명": job_type_list,
                "회사 정보": job_searchfirm_list,
                "회사 위치": job_location_list,
                "채용 마감일": job_deadline_list,
            }
        )

        # DataFrame을 엑셀 파일로 저장
        df.to_excel(selected_job + "_직무코드_채용정보.xlsx", index=False)
        print("엑셀 파일이 정상적으로 다운로드되었는지 확인해보세요!")

    driver.quit()


def scrape_job_data_by_keyword():
    import requests
    from bs4 import BeautifulSoup
    import datetime
    import pandas as pd

    keyword = input("키워드를 입력하세요: ")
    allPage = input("몇 페이지까지 추출하시겠습니까?: ")
    show_experience_anyway = input("경력무관/신입/인턴 관련 채용 정보만 보시겠습니까? (Y/N): ")

    # 데이터를 저장할 빈 리스트 생성
    data = []

    for page in range(1, int(allPage) + 1):
        url = "https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={}&recruitPage={}&recruitSort=relation&recruitPageCount=100".format(
            keyword, page
        )
        headers = {"User-Agent": "Mozilla/5.0"}
        soup = requests.get(url, headers=headers)
        html = BeautifulSoup(soup.text, "html.parser")
        jobs = html.select("div.item_recruit")

        for job in jobs:
            try:
                today = datetime.datetime.now().strftime("%Y-%m-%d")
                title = job.select_one("a")["title"].strip().replace(",", "")
                company = job.select_one("div.area_corp > strong > a").text.strip()
                url = "https://www.saramin.co.kr" + job.select_one("a")["href"]
                deadline = job.select("span.date")[0].text.strip()
                location = job.select("div.job_condition > span")[0].text.strip()
                experience = job.select("div.job_condition > span")[1].text.strip()
                requirement = job.select("div.job_condition > span")[2].text.strip()
                jobtype = job.select("div.job_condition > span")[3].text.strip()

                if show_experience_anyway.upper() == "Y":
                    if (
                        "신입" not in experience
                        and "경력무관" not in experience
                        and "인턴" not in experience
                    ):
                        continue
                else:
                    if "신입" in experience or "경력무관" in experience or "인턴" in experience:
                        continue

                # 데이터를 리스트에 추가
                data.append(
                    [
                        today,
                        title,
                        company,
                        url,
                        deadline,
                        location,
                        experience,
                        requirement,
                        jobtype,
                    ]
                )
            except Exception:
                pass

    # 추출한 데이터를 DataFrame으로 변환
    df = pd.DataFrame(
        data, columns=["날짜", "제목", "회사", "주소", "마감일", "위치", "경력", "요구사항", "직무"]
    )

    # DataFrame을 엑셀 파일로 저장
    df.to_excel(keyword + "_키워드_직무_채용정보.xlsx", index=False)
    print(keyword + "_키워드_직무_채용정보.xlsx 파일이 정상적으로 만들어 졌는지 확인해보세요!")


# 사용자로부터 선택 받기
option = int(input("외국계 기업 직무 검색(1) 또는 희망 기업/직무 관련 키워드 검색(2)을 선택하세요: "))

if option == 1:
    # 직무 검색 선택 시
    # 직무 매핑 함수 호출
    scrape_job_data_by_mapping()
elif option == 2:
    # 키워드 검색 선택 시
    # 키워드 검색 함수 호출
    scrape_job_data_by_keyword()
else:
    print("잘못된 선택입니다.")
