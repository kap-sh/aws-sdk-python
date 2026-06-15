"""Generated from Smithy shape ``com.amazonaws.glue#UpdateCrawlerScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.cron_expression
    import aws_sdk_glue.types.name_string


class UpdateCrawlerScheduleRequest(TypedDict):
    crawler_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the crawler whose schedule to update.</p>"""
    schedule: NotRequired["aws_sdk_glue.types.cron_expression.CronExpression"]
    r"""<p>The updated <code>cron</code> expression used to specify the schedule (see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html\">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCrawlerScheduleRequest) -> dict:
    out: dict = {}
    out["CrawlerName"] = value["crawler_name"]
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCrawlerScheduleRequest:
    out: UpdateCrawlerScheduleRequest = {}  # type: ignore[typeddict-item]
    if "CrawlerName" in data:
        out["crawler_name"] = data["CrawlerName"]
    else:
        raise DeserializationError("UpdateCrawlerScheduleRequest.crawler_name required")
    if "Schedule" in data:
        out["schedule"] = data["Schedule"]
    return out
