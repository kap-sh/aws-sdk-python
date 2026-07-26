"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceResourceOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.space_quick_sight_resource_details
    import capo_quicksight.types.space_quick_sight_resource_type


class SpaceResourceOperation(TypedDict, closed=True):
    resource_type: "capo_quicksight.types.space_quick_sight_resource_type.SpaceQuickSightResourceType"
    """<p>The type of the resource.</p>"""
    resource_details: "capo_quicksight.types.space_quick_sight_resource_details.SpaceQuickSightResourceDetails"
    """<p>The details of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceResourceOperation) -> dict:
    out: dict = {}
    import capo_quicksight.types.space_quick_sight_resource_type

    out["ResourceType"] = (
        capo_quicksight.types.space_quick_sight_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import capo_quicksight.types.space_quick_sight_resource_details

    out["ResourceDetails"] = (
        capo_quicksight.types.space_quick_sight_resource_details.serialize_json(
            value["resource_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> SpaceResourceOperation:
    out: SpaceResourceOperation = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_quicksight.types.space_quick_sight_resource_type

        out["resource_type"] = (
            capo_quicksight.types.space_quick_sight_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError("SpaceResourceOperation.resource_type required")
    if "ResourceDetails" in data:
        import capo_quicksight.types.space_quick_sight_resource_details

        out["resource_details"] = (
            capo_quicksight.types.space_quick_sight_resource_details.deserialize_json(
                data["ResourceDetails"]
            )
        )
    else:
        raise DeserializationError("SpaceResourceOperation.resource_details required")
    return out
