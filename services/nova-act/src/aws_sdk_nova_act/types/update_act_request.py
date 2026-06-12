"""Generated from Smithy shape ``com.amazonaws.novaact#UpdateActRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.act_error
    import aws_sdk_nova_act.types.act_status
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_definition_name


class UpdateActRequest(TypedDict):
    workflow_definition_name: (
        "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the act.</p>"""
    workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run containing the act.</p>"""
    session_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the session containing the act.</p>"""
    act_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the act to update.</p>"""
    status: "aws_sdk_nova_act.types.act_status.ActStatus"
    """<p>The new status to set for the act.</p>"""
    error: NotRequired["aws_sdk_nova_act.types.act_error.ActError"]
    """<p>Error information to associate with the act, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActRequest) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.act_status

    out["status"] = aws_sdk_nova_act.types.act_status.serialize_json(value["status"])
    if "error" in value:
        import aws_sdk_nova_act.types.act_error

        out["error"] = aws_sdk_nova_act.types.act_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> UpdateActRequest:
    out: UpdateActRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_nova_act.types.act_status

        out["status"] = aws_sdk_nova_act.types.act_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateActRequest.status required")
    if "error" in data:
        import aws_sdk_nova_act.types.act_error

        out["error"] = aws_sdk_nova_act.types.act_error.deserialize_json(data["error"])
    return out
