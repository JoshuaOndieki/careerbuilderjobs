from driver import SeleniumDriver


class CBJbot:
    def __init__(self):
        self.jobs = {}
        """
                            self.jobs data structure
        {
        "jobCat":
            [
            "categoryUrl",
            {
            "jobTitle":
                [
                "titleUrl",
                "jobs":
                    [
                        {
                        "postDate": "10 months ago",
                        "title": "Junior Java Software Engineer",
                        "url": "https://be.linkedin.com/jobs/….",
                        "numDaysAgo": "300",
                        "summary": "This is a great opportunity for….",
                        "location": "Leuven, BE",
                        "provider": "Linkedin",
                        "company": "XeniT ",
                        "emailInSummary": [“exampleEmail@company.com]
                        }
                    ]
                ]
            }
            ]
        }
        """
        self.driver = SeleniumDriver().driver

    def get_job_categories(self):
        pass

    def get_job_titles(self):
        pass
