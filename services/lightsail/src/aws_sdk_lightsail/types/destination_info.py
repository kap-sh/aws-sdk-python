"""Generated from Smithy shape ``com.amazonaws.lightsail#DestinationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.non_empty_string


class DestinationInfo(TypedDict):
    id: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the resource created at the destination.</p>"""
    service: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The destination service of the record.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationInfo) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "service" in value:
        out["service"] = value["service"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationInfo:
    out: DestinationInfo = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "service" in data:
        out["service"] = data["service"]
    return out
