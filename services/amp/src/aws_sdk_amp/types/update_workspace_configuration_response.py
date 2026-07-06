"""Generated from Smithy shape ``com.amazonaws.amp#UpdateWorkspaceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.workspace_configuration_status


class UpdateWorkspaceConfigurationResponse(TypedDict, closed=True):
    status: (
        "aws_sdk_amp.types.workspace_configuration_status.WorkspaceConfigurationStatus"
    )
    """<p>The status of the workspace configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.workspace_configuration_status

    out["status"] = aws_sdk_amp.types.workspace_configuration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceConfigurationResponse:
    out: UpdateWorkspaceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_amp.types.workspace_configuration_status

        out["status"] = (
            aws_sdk_amp.types.workspace_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkspaceConfigurationResponse.status required"
        )
    return out
