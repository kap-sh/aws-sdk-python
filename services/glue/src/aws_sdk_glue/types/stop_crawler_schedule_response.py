"""Generated from Smithy shape ``com.amazonaws.glue#StopCrawlerScheduleResponse``."""

from typing_extensions import TypedDict


class StopCrawlerScheduleResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopCrawlerScheduleResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopCrawlerScheduleResponse:
    out: StopCrawlerScheduleResponse = {}  # type: ignore[typeddict-item]
    return out
