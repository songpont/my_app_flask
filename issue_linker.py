# issue_linker.py

import pandas as pd

class IssueLinkerEnhanced:
    def __init__(self):
        self.common_word_mapping = {
            # ... (existing mappings)
            "สิ่งแวดล้อม": ["สิ่งแวดล้อม", "น้ำ", "ขยะ", "การจัดการน้ำ"],
            "น้ำ": ["น้ำ", "การจัดการน้ำ"],
            "อาหาร": ["ความมั่นคงทางอาหาร"],
            "ขยะ": ["ขยะ"],
            "ผู้สูงอายุ": ["ผู้สูงอายุ", "สังคมสูงอายุ"],
            "เยาวชน": ["เด็กและเยาวชน", "เยาวชน"],
            "สุขภาพกาย": ["สุขภาพกาย", "โรคไม่ติดต่อ"],
            "บุหรี่": ["เหล้าบุหรี่", "บุหรี่ไฟฟ้า"],
            "ปัจจัยเสี่ยง": ["เหล้าบุหรี่", "บุหรี่ไฟฟ้า"],
            "เด็ก": ["เด็กและเยาวชน", "เยาวชน"]
        }
        self.p_project_df = pd.read_csv('csv/p_project.csv')
        self.t_project_df = pd.read_csv('csv/t_project.csv')

    def find_related_issues(self, search_term):
        related_issues = set()
        for common_word, issues in self.common_word_mapping.items():
            if search_term in common_word:
                related_issues.update(issues)
            else:
                for issue in issues:
                    if search_term in issue:
                        related_issues.add(issue)

        filtered_p_projects = self.p_project_df[self.p_project_df['p_issue'].isin(related_issues)]
        filtered_t_projects = self.t_project_df[self.t_project_df['t_issue'].isin(related_issues)]

        filtered_p_projects = filtered_p_projects.rename(columns={'pid': 'id', 'p_name': 'name', 'p_issue': 'issue', 'p_sub_district': 'sub_district', 'p_district': 'district', 'p_province': 'province'})
        filtered_t_projects = filtered_t_projects.rename(columns={'tid': 'id', 't_name': 'name', 't_issue': 'issue', 't_sub_district': 'sub_district', 't_district': 'district', 't_province': 'province'})

        filtered_p_projects['source'] = 'p_project'
        filtered_t_projects['source'] = 't_project'

        combined_df = pd.concat([filtered_p_projects, filtered_t_projects], ignore_index=True)
        return combined_df
