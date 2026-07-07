"""Generated from Smithy shape ``com.amazonaws.glue#StartCrawlerScheduleResponse``."""

from typing_extensions import TypedDict


class StartCrawlerScheduleResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCrawlerScheduleResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCrawlerScheduleResponse:
    out: StartCrawlerScheduleResponse = {}  # type: ignore[typeddict-item]
    return out
