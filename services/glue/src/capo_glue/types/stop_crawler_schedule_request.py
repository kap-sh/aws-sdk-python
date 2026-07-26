"""Generated from Smithy shape ``com.amazonaws.glue#StopCrawlerScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.name_string


class StopCrawlerScheduleRequest(TypedDict, closed=True):
    crawler_name: "capo_glue.types.name_string.NameString"
    """<p>Name of the crawler whose schedule state to set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopCrawlerScheduleRequest) -> dict:
    out: dict = {}
    out["CrawlerName"] = value["crawler_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopCrawlerScheduleRequest:
    out: StopCrawlerScheduleRequest = {}  # type: ignore[typeddict-item]
    if "CrawlerName" in data:
        out["crawler_name"] = data["CrawlerName"]
    else:
        raise DeserializationError("StopCrawlerScheduleRequest.crawler_name required")
    return out
