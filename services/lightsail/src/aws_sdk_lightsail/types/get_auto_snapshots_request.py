"""Generated from Smithy shape ``com.amazonaws.lightsail#GetAutoSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class GetAutoSnapshotsRequest(TypedDict, closed=True):
    resource_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the source instance or disk from which to get automatic snapshot information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutoSnapshotsRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutoSnapshotsRequest:
    out: GetAutoSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError("GetAutoSnapshotsRequest.resource_name required")
    return out
