"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuickSightResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.space_quick_sight_resource_details
    import aws_sdk_quicksight.types.space_quick_sight_resource_type


class SpaceQuickSightResource(TypedDict, closed=True):
    resource_type: "aws_sdk_quicksight.types.space_quick_sight_resource_type.SpaceQuickSightResourceType"
    """<p>The type of the QuickSight resource.</p>"""
    resource_details: "aws_sdk_quicksight.types.space_quick_sight_resource_details.SpaceQuickSightResourceDetails"
    """<p>The details of the QuickSight resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceQuickSightResource) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.space_quick_sight_resource_type

    out["resourceType"] = (
        aws_sdk_quicksight.types.space_quick_sight_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import aws_sdk_quicksight.types.space_quick_sight_resource_details

    out["resourceDetails"] = (
        aws_sdk_quicksight.types.space_quick_sight_resource_details.serialize_json(
            value["resource_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> SpaceQuickSightResource:
    out: SpaceQuickSightResource = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_quicksight.types.space_quick_sight_resource_type

        out["resource_type"] = (
            aws_sdk_quicksight.types.space_quick_sight_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError("SpaceQuickSightResource.resource_type required")
    if "resourceDetails" in data:
        import aws_sdk_quicksight.types.space_quick_sight_resource_details

        out["resource_details"] = (
            aws_sdk_quicksight.types.space_quick_sight_resource_details.deserialize_json(
                data["resourceDetails"]
            )
        )
    else:
        raise DeserializationError("SpaceQuickSightResource.resource_details required")
    return out
