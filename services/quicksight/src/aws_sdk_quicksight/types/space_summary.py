"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_quicksight.types.integer
    import aws_sdk_quicksight.types.long
    import aws_sdk_quicksight.types.public_space_arn
    import aws_sdk_quicksight.types.public_space_id
    import aws_sdk_quicksight.types.space_description
    import aws_sdk_quicksight.types.space_name


class SpaceSummary(TypedDict, closed=True):
    space_id: "aws_sdk_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space.</p>"""
    space_arn: NotRequired["aws_sdk_quicksight.types.public_space_arn.PublicSpaceArn"]
    """<p>The ARN of the space.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.space_name.SpaceName"]
    """<p>The display name of the space.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.space_description.SpaceDescription"
    ]
    """<p>The description of the space.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the space was last updated.</p>"""
    consumed_source_size: NotRequired["aws_sdk_quicksight.types.long.Long"]
    """<p>The total consumed source size in bytes.</p>"""
    consumed_source_doc_count: NotRequired["aws_sdk_quicksight.types.integer.Integer"]
    """<p>The number of consumed source documents.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the space was created.</p>"""
    created_by: NotRequired["str"]
    """<p>The user who created the space.</p>"""
    created_by_arn: NotRequired["str"]
    """<p>The ARN of the user who created the space.</p>"""
    resources_count: NotRequired["aws_sdk_quicksight.types.integer.Integer"]
    """<p>The number of resources in the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceSummary) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "space_arn" in value:
        out["spaceArn"] = value["space_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "updated_at" in value:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "consumed_source_size" in value:
        out["consumedSourceSize"] = value["consumed_source_size"]
    if "consumed_source_doc_count" in value:
        out["consumedSourceDocCount"] = value["consumed_source_doc_count"]
    if "created_at" in value:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["createdAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_by_arn" in value:
        out["createdByArn"] = value["created_by_arn"]
    if "resources_count" in value:
        out["resourcesCount"] = value["resources_count"]
    return out


def deserialize_json(data: dict) -> SpaceSummary:
    out: SpaceSummary = {}  # type: ignore[typeddict-item]
    if "spaceId" in data:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("SpaceSummary.space_id required")
    if "spaceArn" in data:
        out["space_arn"] = data["spaceArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
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
    if "createdAt" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "createdByArn" in data:
        out["created_by_arn"] = data["createdByArn"]
    if "resourcesCount" in data:
        out["resources_count"] = data["resourcesCount"]
    return out
