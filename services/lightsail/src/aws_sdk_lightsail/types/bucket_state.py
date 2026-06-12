"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.string


class BucketState(TypedDict):
    code: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The state code of the bucket.</p> <p>The following codes are possible:</p> <ul> <li> <p> <code>OK</code> - The bucket is in a running state.</p> </li> <li> <p> <code>Unknown</code> - Creation of the bucket might have timed-out. You might want to delete the bucket and create a new one.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>A message that describes the state of the bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketState) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BucketState:
    out: BucketState = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
