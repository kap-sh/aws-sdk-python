"""Generated from Smithy shape ``com.amazonaws.iot#RelatedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.resource_identifier
    import capo_iot.types.resource_type
    import capo_iot.types.string_map


class RelatedResource(TypedDict, closed=True):
    resource_type: NotRequired["capo_iot.types.resource_type.ResourceType"]
    """<p>The type of resource.</p>"""
    resource_identifier: NotRequired[
        "capo_iot.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>Information that identifies the resource.</p>"""
    additional_info: NotRequired["capo_iot.types.string_map.StringMap"]
    """<p>Other information about the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedResource) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_iot.types.resource_type

        out["resourceType"] = capo_iot.types.resource_type.serialize_json(
            value["resource_type"]
        )
    if "resource_identifier" in value:
        import capo_iot.types.resource_identifier

        out["resourceIdentifier"] = capo_iot.types.resource_identifier.serialize_json(
            value["resource_identifier"]
        )
    if "additional_info" in value:
        import capo_iot.types.string_map

        out["additionalInfo"] = capo_iot.types.string_map.serialize_json(
            value["additional_info"]
        )
    return out


def deserialize_json(data: dict) -> RelatedResource:
    out: RelatedResource = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import capo_iot.types.resource_type

        out["resource_type"] = capo_iot.types.resource_type.deserialize_json(
            data["resourceType"]
        )
    if "resourceIdentifier" in data:
        import capo_iot.types.resource_identifier

        out["resource_identifier"] = (
            capo_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    if "additionalInfo" in data:
        import capo_iot.types.string_map

        out["additional_info"] = capo_iot.types.string_map.deserialize_json(
            data["additionalInfo"]
        )
    return out
