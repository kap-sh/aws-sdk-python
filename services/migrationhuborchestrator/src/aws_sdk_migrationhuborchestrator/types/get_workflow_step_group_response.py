"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetWorkflowStepGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_migrationhuborchestrator.types.owner
    import aws_sdk_migrationhuborchestrator.types.step_group_id
    import aws_sdk_migrationhuborchestrator.types.step_group_status
    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.tools_list


class GetWorkflowStepGroupResponse(TypedDict):
    id: NotRequired["aws_sdk_migrationhuborchestrator.types.step_group_id.StepGroupId"]
    """<p>The ID of the step group.</p>"""
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step group.</p>"""
    description: NotRequired["str"]
    """<p>The description of the step group.</p>"""
    status: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.step_group_status.StepGroupStatus"
    ]
    """<p>The status of the step group.</p>"""
    owner: NotRequired["aws_sdk_migrationhuborchestrator.types.owner.Owner"]
    """<p>The owner of the step group.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step group was created.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step group was last modified.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the step group ended.</p>"""
    tools: NotRequired["aws_sdk_migrationhuborchestrator.types.tools_list.ToolsList"]
    """<p>List of AWS services utilized in a migration workflow.</p>"""
    previous: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The previous step group.</p>"""
    next: NotRequired["aws_sdk_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowStepGroupResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "creation_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["lastModifiedTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["endTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "tools" in value:
        import aws_sdk_migrationhuborchestrator.types.tools_list

        out["tools"] = aws_sdk_migrationhuborchestrator.types.tools_list.serialize_json(
            value["tools"]
        )
    if "previous" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["previous"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    if "next" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["next"] = aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    return out


def deserialize_json(data: dict) -> GetWorkflowStepGroupResponse:
    out: GetWorkflowStepGroupResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        out["status"] = data["status"]
    if "owner" in data:
        out["owner"] = data["owner"]
    if "creationTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "lastModifiedTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "tools" in data:
        import aws_sdk_migrationhuborchestrator.types.tools_list

        out["tools"] = (
            aws_sdk_migrationhuborchestrator.types.tools_list.deserialize_json(
                data["tools"]
            )
        )
    if "previous" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["previous"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    if "next" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["next"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["next"]
            )
        )
    return out
