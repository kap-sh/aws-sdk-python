"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_quicksight.types.integer
    import aws_sdk_quicksight.types.long
    import aws_sdk_quicksight.types.space_description
    import aws_sdk_quicksight.types.space_name
    import aws_sdk_quicksight.types.space_quick_sight_resources


class SpaceDetails(TypedDict):
    name: NotRequired["aws_sdk_quicksight.types.space_name.SpaceName"]
    """<p>The display name of the space.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.space_description.SpaceDescription"
    ]
    """<p>The description of the space.</p>"""
    resources: NotRequired[
        "aws_sdk_quicksight.types.space_quick_sight_resources.SpaceQuickSightResources"
    ]
    """<p>The resources in the space.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the space was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the space was last updated.</p>"""
    consumed_source_size: NotRequired["aws_sdk_quicksight.types.long.Long"]
    """<p>The total consumed source size in bytes.</p>"""
    consumed_source_doc_count: NotRequired["aws_sdk_quicksight.types.integer.Integer"]
    """<p>The number of consumed source documents.</p>"""
    created_by: NotRequired["str"]
    """<p>The user who created the space.</p>"""
    created_by_arn: NotRequired["str"]
    """<p>The ARN of the user who created the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "resources" in value:
        import aws_sdk_quicksight.types.space_quick_sight_resources

        out["resources"] = (
            aws_sdk_quicksight.types.space_quick_sight_resources.serialize_json(
                value["resources"]
            )
        )
    if "created_at" in value:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["createdAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "consumed_source_size" in value:
        out["consumedSourceSize"] = value["consumed_source_size"]
    if "consumed_source_doc_count" in value:
        out["consumedSourceDocCount"] = value["consumed_source_doc_count"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_by_arn" in value:
        out["createdByArn"] = value["created_by_arn"]
    return out


def deserialize_json(data: dict) -> SpaceDetails:
    out: SpaceDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "resources" in data:
        import aws_sdk_quicksight.types.space_quick_sight_resources

        out["resources"] = (
            aws_sdk_quicksight.types.space_quick_sight_resources.deserialize_json(
                data["resources"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "consumedSourceSize" in data:
        out["consumed_source_size"] = data["consumedSourceSize"]
    if "consumedSourceDocCount" in data:
        out["consumed_source_doc_count"] = data["consumedSourceDocCount"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "createdByArn" in data:
        out["created_by_arn"] = data["createdByArn"]
    return out
