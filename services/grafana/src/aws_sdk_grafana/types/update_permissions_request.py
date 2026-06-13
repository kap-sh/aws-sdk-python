"""Generated from Smithy shape ``com.amazonaws.grafana#UpdatePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.update_instruction_batch
    import aws_sdk_grafana.types.workspace_id


class UpdatePermissionsRequest(TypedDict):
    update_instruction_batch: (
        "aws_sdk_grafana.types.update_instruction_batch.UpdateInstructionBatch"
    )
    """<p>An array of structures that contain the permission updates to make.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePermissionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.update_instruction_batch

    out["updateInstructionBatch"] = (
        aws_sdk_grafana.types.update_instruction_batch.serialize_json(
            value["update_instruction_batch"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePermissionsRequest:
    out: UpdatePermissionsRequest = {}  # type: ignore[typeddict-item]
    if "updateInstructionBatch" in data:
        import aws_sdk_grafana.types.update_instruction_batch

        out["update_instruction_batch"] = (
            aws_sdk_grafana.types.update_instruction_batch.deserialize_json(
                data["updateInstructionBatch"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePermissionsRequest.update_instruction_batch required"
        )
    return out
