"""Generated from Smithy shape ``com.amazonaws.glue#StartCrawlerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class StartCrawlerRequest(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Name of the crawler to start.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCrawlerRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCrawlerRequest:
    out: StartCrawlerRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartCrawlerRequest.name required")
    return out
