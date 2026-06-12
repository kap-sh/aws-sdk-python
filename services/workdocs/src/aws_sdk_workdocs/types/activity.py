"""Generated from Smithy shape ``com.amazonaws.workdocs#Activity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.activity_type
    import aws_sdk_workdocs.types.boolean_type
    import aws_sdk_workdocs.types.comment_metadata
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.participants
    import aws_sdk_workdocs.types.resource_metadata
    import aws_sdk_workdocs.types.timestamp_type
    import aws_sdk_workdocs.types.user_metadata


class Activity(TypedDict):
    type: NotRequired["aws_sdk_workdocs.types.activity_type.ActivityType"]
    """<p>The activity type.</p>"""
    time_stamp: NotRequired["aws_sdk_workdocs.types.timestamp_type.TimestampType"]
    """<p>The timestamp when the action was performed.</p>"""
    is_indirect_activity: "aws_sdk_workdocs.types.boolean_type.BooleanType"
    """<p>Indicates whether an activity is indirect or direct. An indirect activity results from a direct activity performed on a parent resource. For example, sharing a parent folder (the direct activity) shares all of the subfolders and documents within the parent folder (the indirect activity).</p>"""
    organization_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the organization.</p>"""
    initiator: NotRequired["aws_sdk_workdocs.types.user_metadata.UserMetadata"]
    """<p>The user who performed the action.</p>"""
    participants: NotRequired["aws_sdk_workdocs.types.participants.Participants"]
    """<p>The list of users or groups impacted by this action. This is an optional field and is filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED, DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.</p>"""
    resource_metadata: NotRequired[
        "aws_sdk_workdocs.types.resource_metadata.ResourceMetadata"
    ]
    """<p>The metadata of the resource involved in the user action.</p>"""
    original_parent: NotRequired[
        "aws_sdk_workdocs.types.resource_metadata.ResourceMetadata"
    ]
    """<p>The original parent of the resource. This is an optional field and is filled for move activities.</p>"""
    comment_metadata: NotRequired[
        "aws_sdk_workdocs.types.comment_metadata.CommentMetadata"
    ]
    """<p>Metadata of the commenting activity. This is an optional field and is filled for commenting activities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Activity) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_workdocs.types.activity_type

        out["Type"] = aws_sdk_workdocs.types.activity_type.serialize_json(value["type"])
    if "time_stamp" in value:
        import aws_sdk_workdocs.types.timestamp_type

        out["TimeStamp"] = aws_sdk_workdocs.types.timestamp_type.serialize_json(
            value["time_stamp"]
        )
    out["IsIndirectActivity"] = value.get("is_indirect_activity", False)
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "initiator" in value:
        import aws_sdk_workdocs.types.user_metadata

        out["Initiator"] = aws_sdk_workdocs.types.user_metadata.serialize_json(
            value["initiator"]
        )
    if "participants" in value:
        import aws_sdk_workdocs.types.participants

        out["Participants"] = aws_sdk_workdocs.types.participants.serialize_json(
            value["participants"]
        )
    if "resource_metadata" in value:
        import aws_sdk_workdocs.types.resource_metadata

        out["ResourceMetadata"] = (
            aws_sdk_workdocs.types.resource_metadata.serialize_json(
                value["resource_metadata"]
            )
        )
    if "original_parent" in value:
        import aws_sdk_workdocs.types.resource_metadata

        out["OriginalParent"] = aws_sdk_workdocs.types.resource_metadata.serialize_json(
            value["original_parent"]
        )
    if "comment_metadata" in value:
        import aws_sdk_workdocs.types.comment_metadata

        out["CommentMetadata"] = aws_sdk_workdocs.types.comment_metadata.serialize_json(
            value["comment_metadata"]
        )
    return out


def deserialize_json(data: dict) -> Activity:
    out: Activity = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_workdocs.types.activity_type

        out["type"] = aws_sdk_workdocs.types.activity_type.deserialize_json(
            data["Type"]
        )
    if "TimeStamp" in data:
        import aws_sdk_workdocs.types.timestamp_type

        out["time_stamp"] = aws_sdk_workdocs.types.timestamp_type.deserialize_json(
            data["TimeStamp"]
        )
    if "IsIndirectActivity" in data:
        out["is_indirect_activity"] = data["IsIndirectActivity"]
    else:
        out["is_indirect_activity"] = False
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    if "Initiator" in data:
        import aws_sdk_workdocs.types.user_metadata

        out["initiator"] = aws_sdk_workdocs.types.user_metadata.deserialize_json(
            data["Initiator"]
        )
    if "Participants" in data:
        import aws_sdk_workdocs.types.participants

        out["participants"] = aws_sdk_workdocs.types.participants.deserialize_json(
            data["Participants"]
        )
    if "ResourceMetadata" in data:
        import aws_sdk_workdocs.types.resource_metadata

        out["resource_metadata"] = (
            aws_sdk_workdocs.types.resource_metadata.deserialize_json(
                data["ResourceMetadata"]
            )
        )
    if "OriginalParent" in data:
        import aws_sdk_workdocs.types.resource_metadata

        out["original_parent"] = (
            aws_sdk_workdocs.types.resource_metadata.deserialize_json(
                data["OriginalParent"]
            )
        )
    if "CommentMetadata" in data:
        import aws_sdk_workdocs.types.comment_metadata

        out["comment_metadata"] = (
            aws_sdk_workdocs.types.comment_metadata.deserialize_json(
                data["CommentMetadata"]
            )
        )
    return out
