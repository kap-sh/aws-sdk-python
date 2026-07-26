"""Generated from Smithy shape ``com.amazonaws.opensearch#ChangeProgressStage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.change_progress_stage_name
    import capo_opensearch.types.change_progress_stage_status
    import capo_opensearch.types.description
    import capo_opensearch.types.last_updated


class ChangeProgressStage(TypedDict, closed=True):
    name: NotRequired[
        "capo_opensearch.types.change_progress_stage_name.ChangeProgressStageName"
    ]
    """<p>The name of the stage.</p>"""
    status: NotRequired[
        "capo_opensearch.types.change_progress_stage_status.ChangeProgressStageStatus"
    ]
    """<p>The status of the stage.</p>"""
    description: NotRequired["capo_opensearch.types.description.Description"]
    """<p>The description of the stage.</p>"""
    last_updated: NotRequired["capo_opensearch.types.last_updated.LastUpdated"]
    """<p>The most recent updated timestamp of the stage.</p>"""


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
        import capo_opensearch.types.last_updated

        out["LastUpdated"] = capo_opensearch.types.last_updated.serialize_json(
            value["last_updated"]
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
        import capo_opensearch.types.last_updated

        out["last_updated"] = capo_opensearch.types.last_updated.deserialize_json(
            data["LastUpdated"]
        )
    return out
