"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UpdateWorkflowStepGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.tools_list


class UpdateWorkflowStepGroupResponse(TypedDict):
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step group.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    description: NotRequired["str"]
    """<p>The description of the step group.</p>"""
    tools: NotRequired["aws_sdk_migrationhuborchestrator.types.tools_list.ToolsList"]
    """<p>List of AWS services utilized in a migration workflow.</p>"""
    next: NotRequired["aws_sdk_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step group.</p>"""
    previous: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The previous step group.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step group was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkflowStepGroupResponse) -> dict:
    out: dict = {}
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "tools" in value:
        import aws_sdk_migrationhuborchestrator.types.tools_list

        out["tools"] = aws_sdk_migrationhuborchestrator.types.tools_list.serialize_json(
            value["tools"]
        )
    if "next" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["next"] = aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    if "previous" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["previous"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["lastModifiedTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkflowStepGroupResponse:
    out: UpdateWorkflowStepGroupResponse = {}  # type: ignore[typeddict-item]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "description" in data:
        out["description"] = data["description"]
    if "tools" in data:
        import aws_sdk_migrationhuborchestrator.types.tools_list

        out["tools"] = (
            aws_sdk_migrationhuborchestrator.types.tools_list.deserialize_json(
                data["tools"]
            )
        )
    if "next" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["next"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["next"]
            )
        )
    if "previous" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["previous"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    if "lastModifiedTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    return out
