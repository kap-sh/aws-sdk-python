"""Generated from Smithy shape ``com.amazonaws.amp#UpdateWorkspaceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.workspace_configuration_status


class UpdateWorkspaceConfigurationResponse(TypedDict, closed=True):
    status: "capo_amp.types.workspace_configuration_status.WorkspaceConfigurationStatus"
    """<p>The status of the workspace configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types.workspace_configuration_status

    out["status"] = capo_amp.types.workspace_configuration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceConfigurationResponse:
    out: UpdateWorkspaceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_amp.types.workspace_configuration_status

        out["status"] = capo_amp.types.workspace_configuration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError(
            "UpdateWorkspaceConfigurationResponse.status required"
        )
    return out
