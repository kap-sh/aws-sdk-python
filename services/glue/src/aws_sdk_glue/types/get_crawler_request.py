"""Generated from Smithy shape ``com.amazonaws.glue#GetCrawlerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class GetCrawlerRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the crawler to retrieve metadata for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCrawlerRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCrawlerRequest:
    out: GetCrawlerRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetCrawlerRequest.name required")
    return out
