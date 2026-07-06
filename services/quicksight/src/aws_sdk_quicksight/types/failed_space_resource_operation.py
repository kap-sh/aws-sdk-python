"""Generated from Smithy shape ``com.amazonaws.quicksight#FailedSpaceResourceOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.space_quick_sight_resource_details
    import aws_sdk_quicksight.types.space_quick_sight_resource_type


class FailedSpaceResourceOperation(TypedDict, closed=True):
    resource_type: "aws_sdk_quicksight.types.space_quick_sight_resource_type.SpaceQuickSightResourceType"
    """<p>The type of the resource.</p>"""
    resource_details: NotRequired[
        "aws_sdk_quicksight.types.space_quick_sight_resource_details.SpaceQuickSightResourceDetails"
    ]
    """<p>The details of the resource.</p>"""
    error_message: "str"
    """<p>The error message that describes why the operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedSpaceResourceOperation) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.space_quick_sight_resource_type

    out["ResourceType"] = (
        aws_sdk_quicksight.types.space_quick_sight_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    if "resource_details" in value:
        import aws_sdk_quicksight.types.space_quick_sight_resource_details

        out["ResourceDetails"] = (
            aws_sdk_quicksight.types.space_quick_sight_resource_details.serialize_json(
                value["resource_details"]
            )
        )
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedSpaceResourceOperation:
    out: FailedSpaceResourceOperation = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import aws_sdk_quicksight.types.space_quick_sight_resource_type

        out["resource_type"] = (
            aws_sdk_quicksight.types.space_quick_sight_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError(
            "FailedSpaceResourceOperation.resource_type required"
        )
    if "ResourceDetails" in data:
        import aws_sdk_quicksight.types.space_quick_sight_resource_details

        out["resource_details"] = (
            aws_sdk_quicksight.types.space_quick_sight_resource_details.deserialize_json(
                data["ResourceDetails"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    else:
        raise DeserializationError(
            "FailedSpaceResourceOperation.error_message required"
        )
    return out
