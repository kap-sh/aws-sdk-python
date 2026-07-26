"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StopLoggingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.string


class StopLoggingRequest(TypedDict, closed=True):
    name: "capo_cloudtrail.types.string.String"
    """<p>Specifies the name or the CloudTrail ARN of the trail for which CloudTrail will stop logging Amazon Web Services API calls. The following is the format of a trail ARN.</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopLoggingRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopLoggingRequest:
    out: StopLoggingRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StopLoggingRequest.name required")
    return out
