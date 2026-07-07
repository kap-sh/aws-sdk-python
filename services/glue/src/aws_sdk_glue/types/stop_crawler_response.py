"""Generated from Smithy shape ``com.amazonaws.glue#StopCrawlerResponse``."""

from typing_extensions import TypedDict


class StopCrawlerResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopCrawlerResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopCrawlerResponse:
    out: StopCrawlerResponse = {}  # type: ignore[typeddict-item]
    return out
