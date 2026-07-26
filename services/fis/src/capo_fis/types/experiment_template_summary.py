"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.creation_time
    import capo_fis.types.experiment_template_description
    import capo_fis.types.experiment_template_id
    import capo_fis.types.last_update_time
    import capo_fis.types.resource_arn
    import capo_fis.types.tag_map


class ExperimentTemplateSummary(TypedDict, closed=True):
    id: NotRequired["capo_fis.types.experiment_template_id.ExperimentTemplateId"]
    """<p>The ID of the experiment template.</p>"""
    arn: NotRequired["capo_fis.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the experiment template.</p>"""
    description: NotRequired[
        "capo_fis.types.experiment_template_description.ExperimentTemplateDescription"
    ]
    """<p>The description of the experiment template.</p>"""
    creation_time: NotRequired["capo_fis.types.creation_time.CreationTime"]
    """<p>The time that the experiment template was created.</p>"""
    last_update_time: NotRequired["capo_fis.types.last_update_time.LastUpdateTime"]
    """<p>The time that the experiment template was last updated.</p>"""
    tags: NotRequired["capo_fis.types.tag_map.TagMap"]
    """<p>The tags for the experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_time" in value:
        import capo_fis.types.creation_time

        out["creationTime"] = capo_fis.types.creation_time.serialize_json(
            value["creation_time"]
        )
    if "last_update_time" in value:
        import capo_fis.types.last_update_time

        out["lastUpdateTime"] = capo_fis.types.last_update_time.serialize_json(
            value["last_update_time"]
        )
    if "tags" in value:
        import capo_fis.types.tag_map

        out["tags"] = capo_fis.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ExperimentTemplateSummary:
    out: ExperimentTemplateSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationTime" in data:
        import capo_fis.types.creation_time

        out["creation_time"] = capo_fis.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdateTime" in data:
        import capo_fis.types.last_update_time

        out["last_update_time"] = capo_fis.types.last_update_time.deserialize_json(
            data["lastUpdateTime"]
        )
    if "tags" in data:
        import capo_fis.types.tag_map

        out["tags"] = capo_fis.types.tag_map.deserialize_json(data["tags"])
    return out
