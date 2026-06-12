"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateGUISessionAccessDetailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class CreateGUISessionAccessDetailsRequest(TypedDict):
    resource_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The resource name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGUISessionAccessDetailsRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGUISessionAccessDetailsRequest:
    out: CreateGUISessionAccessDetailsRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError(
            "CreateGUISessionAccessDetailsRequest.resource_name required"
        )
    return out
