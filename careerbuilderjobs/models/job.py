"""
    Job model
"""


class Job():
    """
        Creates a Job objects.
        **kwargs:
            job_id: A unique identifier for the job.
            post_date: Period since job was posted.
            title: The title of the job.
            url: url linking to this specific job.
            num_days_ago: days since job was posted.
            summary: A summary of the job.
            location: Location job is offered.
            provider: Channel where the job was scraped from.
            company: The entity offering this job.
            email_in_summary: Email found in the job description.
    """

    def __init__(self, **kwargs):
        """
            Job object initializer.
            Returns:
                Object
        """
        self.job_id = kwargs['job_id']
        self.post_date = kwargs['post_date']
        self.title = kwargs['title']
        self.url = kwargs['url']
        self.num_days_ago = kwargs['num_days_ago']
        self.summary = kwargs['summary']
        self.location = kwargs['location']
        self.provider = kwargs['provider']
        self.company = kwargs['company']
        self.email_in_summary = kwargs['email_in_summary']

    def __repr__(self):
        return(self.title + ', ' + self.company)
