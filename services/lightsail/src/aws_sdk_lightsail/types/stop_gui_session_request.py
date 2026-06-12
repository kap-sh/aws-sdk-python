"""Generated from Smithy shape ``com.amazonaws.lightsail#StopGUISessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class StopGUISessionRequest(TypedDict):
    resource_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The resource name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopGUISessionRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopGUISessionRequest:
    out: StopGUISessionRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError("StopGUISessionRequest.resource_name required")
    return out
