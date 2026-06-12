"""Generated from Smithy shape ``com.amazonaws.panorama#ProvisionDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.description
    import aws_sdk_panorama.types.device_name
    import aws_sdk_panorama.types.network_payload
    import aws_sdk_panorama.types.tag_map


class ProvisionDeviceRequest(TypedDict):
    name: "aws_sdk_panorama.types.device_name.DeviceName"
    """<p>A name for the device.</p>"""
    description: NotRequired["aws_sdk_panorama.types.description.Description"]
    """<p>A description for the device.</p>"""
    tags: NotRequired["aws_sdk_panorama.types.tag_map.TagMap"]
    """<p>Tags for the device.</p>"""
    networking_configuration: NotRequired[
        "aws_sdk_panorama.types.network_payload.NetworkPayload"
    ]
    """<p>A networking configuration for the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionDeviceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_panorama.types.tag_map

        out["Tags"] = aws_sdk_panorama.types.tag_map.serialize_json(value["tags"])
    if "networking_configuration" in value:
        import aws_sdk_panorama.types.network_payload

        out["NetworkingConfiguration"] = (
            aws_sdk_panorama.types.network_payload.serialize_json(
                value["networking_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProvisionDeviceRequest:
    out: ProvisionDeviceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ProvisionDeviceRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_panorama.types.tag_map

        out["tags"] = aws_sdk_panorama.types.tag_map.deserialize_json(data["Tags"])
    if "NetworkingConfiguration" in data:
        import aws_sdk_panorama.types.network_payload

        out["networking_configuration"] = (
            aws_sdk_panorama.types.network_payload.deserialize_json(
                data["NetworkingConfiguration"]
            )
        )
    return out
