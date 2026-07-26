"""Generated from Smithy shape ``com.amazonaws.panorama#ProvisionDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.description
    import capo_panorama.types.device_name
    import capo_panorama.types.network_payload
    import capo_panorama.types.tag_map


class ProvisionDeviceRequest(TypedDict, closed=True):
    name: "capo_panorama.types.device_name.DeviceName"
    """<p>A name for the device.</p>"""
    description: NotRequired["capo_panorama.types.description.Description"]
    """<p>A description for the device.</p>"""
    tags: NotRequired["capo_panorama.types.tag_map.TagMap"]
    """<p>Tags for the device.</p>"""
    networking_configuration: NotRequired[
        "capo_panorama.types.network_payload.NetworkPayload"
    ]
    """<p>A networking configuration for the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionDeviceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_panorama.types.tag_map

        out["Tags"] = capo_panorama.types.tag_map.serialize_json(value["tags"])
    if "networking_configuration" in value:
        import capo_panorama.types.network_payload

        out["NetworkingConfiguration"] = (
            capo_panorama.types.network_payload.serialize_json(
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
        import capo_panorama.types.tag_map

        out["tags"] = capo_panorama.types.tag_map.deserialize_json(data["Tags"])
    if "NetworkingConfiguration" in data:
        import capo_panorama.types.network_payload

        out["networking_configuration"] = (
            capo_panorama.types.network_payload.deserialize_json(
                data["NetworkingConfiguration"]
            )
        )
    return out
