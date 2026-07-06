"""Generated from Smithy shape ``com.amazonaws.osis#ChangeProgressStage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.change_progress_stage_statuses
    import aws_sdk_osis.types.string
    import aws_sdk_osis.types.timestamp


class ChangeProgressStage(TypedDict, closed=True):
    name: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The name of the stage.</p>"""
    status: NotRequired[
        "aws_sdk_osis.types.change_progress_stage_statuses.ChangeProgressStageStatuses"
    ]
    """<p>The current status of the stage that the change is in.</p>"""
    description: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>A description of the stage.</p>"""
    last_updated_at: NotRequired["aws_sdk_osis.types.timestamp.Timestamp"]
    """<p>The most recent updated timestamp of the stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStage) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_osis.types.change_progress_stage_statuses

        out["Status"] = (
            aws_sdk_osis.types.change_progress_stage_statuses.serialize_json(
                value["status"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "last_updated_at" in value:
        import aws_sdk_osis.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_osis.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ChangeProgressStage:
    out: ChangeProgressStage = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_osis.types.change_progress_stage_statuses

        out["status"] = (
            aws_sdk_osis.types.change_progress_stage_statuses.deserialize_json(
                data["Status"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "LastUpdatedAt" in data:
        import aws_sdk_osis.types.timestamp

        out["last_updated_at"] = aws_sdk_osis.types.timestamp.deserialize_json(
            data["LastUpdatedAt"]
        )
    return out
