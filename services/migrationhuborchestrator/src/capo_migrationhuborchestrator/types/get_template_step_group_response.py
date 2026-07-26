"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetTemplateStepGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_migrationhuborchestrator.types.step_group_status
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.tools_list


class GetTemplateStepGroupResponse(TypedDict, closed=True):
    template_id: NotRequired["str"]
    """<p>The ID of the template.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step group.</p>"""
    description: NotRequired["str"]
    """<p>The description of the step group.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.step_group_status.StepGroupStatus"
    ]
    """<p>The status of the step group.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step group was created.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step group was last modified.</p>"""
    tools: NotRequired["capo_migrationhuborchestrator.types.tools_list.ToolsList"]
    """<p>List of AWS services utilized in a migration workflow.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step group.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateStepGroupResponse) -> dict:
    out: dict = {}
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["lastModifiedTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    if "tools" in value:
        import capo_migrationhuborchestrator.types.tools_list

        out["tools"] = capo_migrationhuborchestrator.types.tools_list.serialize_json(
            value["tools"]
        )
    if "previous" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    if "next" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    return out


def deserialize_json(data: dict) -> GetTemplateStepGroupResponse:
    out: GetTemplateStepGroupResponse = {}  # type: ignore[typeddict-item]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        out["status"] = data["status"]
    if "creationTime" in data:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "lastModifiedTime" in data:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if "tools" in data:
        import capo_migrationhuborchestrator.types.tools_list

        out["tools"] = capo_migrationhuborchestrator.types.tools_list.deserialize_json(
            data["tools"]
        )
    if "previous" in data:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    if "next" in data:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.deserialize_json(
            data["next"]
        )
    return out
