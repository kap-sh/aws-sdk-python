"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.version_number
    import capo_imagebuilder.types.workflow_name_arn
    import capo_imagebuilder.types.workflow_state
    import capo_imagebuilder.types.workflow_type


class WorkflowSummary(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.workflow_name_arn.WorkflowNameArn"]
    """<p>The Amazon Resource Name (ARN) of the workflow resource.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the workflow.</p>"""
    version: NotRequired["capo_imagebuilder.types.version_number.VersionNumber"]
    """<p>The version of the workflow.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Describes the workflow.</p>"""
    change_description: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The change description for the current version of the workflow resource.</p>"""
    type: NotRequired["capo_imagebuilder.types.workflow_type.WorkflowType"]
    """<p>The image creation stage that this workflow applies to. Image Builder currently supports build and test stage workflows.</p>"""
    owner: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the workflow resource.</p>"""
    state: NotRequired["capo_imagebuilder.types.workflow_state.WorkflowState"]
    """<p>Describes the current state of the workflow resource.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The original creation date of the workflow resource.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Contains a list of tags that are defined for the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
    if "change_description" in value:
        out["changeDescription"] = value["change_description"]
    if "type" in value:
        import capo_imagebuilder.types.workflow_type

        out["type"] = capo_imagebuilder.types.workflow_type.serialize_json(
            value["type"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "state" in value:
        import capo_imagebuilder.types.workflow_state

        out["state"] = capo_imagebuilder.types.workflow_state.serialize_json(
            value["state"]
        )
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> WorkflowSummary:
    out: WorkflowSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    if "description" in data:
        out["description"] = data["description"]
    if "changeDescription" in data:
        out["change_description"] = data["changeDescription"]
    if "type" in data:
        import capo_imagebuilder.types.workflow_type

        out["type"] = capo_imagebuilder.types.workflow_type.deserialize_json(
            data["type"]
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "state" in data:
        import capo_imagebuilder.types.workflow_state

        out["state"] = capo_imagebuilder.types.workflow_state.deserialize_json(
            data["state"]
        )
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    return out
