"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ChangeProgressStage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.change_progress_stage_name
    import aws_sdk_elasticsearch_service.types.change_progress_stage_status
    import aws_sdk_elasticsearch_service.types.description
    import aws_sdk_elasticsearch_service.types.last_updated


class ChangeProgressStage(TypedDict):
    name: NotRequired[
        "aws_sdk_elasticsearch_service.types.change_progress_stage_name.ChangeProgressStageName"
    ]
    """<p>The name of the specific progress stage.</p>"""
    status: NotRequired[
        "aws_sdk_elasticsearch_service.types.change_progress_stage_status.ChangeProgressStageStatus"
    ]
    """<p>The overall status of a specific progress stage.</p>"""
    description: NotRequired[
        "aws_sdk_elasticsearch_service.types.description.Description"
    ]
    """<p>The description of the progress stage.</p>"""
    last_updated: NotRequired[
        "aws_sdk_elasticsearch_service.types.last_updated.LastUpdated"
    ]
    """<p>The last updated timestamp of the progress stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStage) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "description" in value:
        out["Description"] = value["description"]
    if "last_updated" in value:
        import aws_sdk_elasticsearch_service.types.last_updated

        out["LastUpdated"] = (
            aws_sdk_elasticsearch_service.types.last_updated.serialize_json(
                value["last_updated"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChangeProgressStage:
    out: ChangeProgressStage = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LastUpdated" in data:
        import aws_sdk_elasticsearch_service.types.last_updated

        out["last_updated"] = (
            aws_sdk_elasticsearch_service.types.last_updated.deserialize_json(
                data["LastUpdated"]
            )
        )
    return out
