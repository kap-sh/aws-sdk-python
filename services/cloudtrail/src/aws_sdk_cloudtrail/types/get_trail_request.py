"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetTrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.string


class GetTrailRequest(TypedDict, closed=True):
    name: "aws_sdk_cloudtrail.types.string.String"
    """<p>The name or the Amazon Resource Name (ARN) of the trail for which you want to retrieve settings information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTrailRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTrailRequest:
    out: GetTrailRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetTrailRequest.name required")
    return out
