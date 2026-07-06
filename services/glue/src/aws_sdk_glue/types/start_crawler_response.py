"""Generated from Smithy shape ``com.amazonaws.glue#StartCrawlerResponse``."""

from typing_extensions import TypedDict


class StartCrawlerResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCrawlerResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCrawlerResponse:
    out: StartCrawlerResponse = {}  # type: ignore[typeddict-item]
    return out
