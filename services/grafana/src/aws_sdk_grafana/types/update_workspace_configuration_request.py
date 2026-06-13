"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateWorkspaceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.grafana_version
    import aws_sdk_grafana.types.overridable_configuration_json
    import aws_sdk_grafana.types.workspace_id


class UpdateWorkspaceConfigurationRequest(TypedDict):
    configuration: "aws_sdk_grafana.types.overridable_configuration_json.OverridableConfigurationJson"
    """<p>The new configuration string for the workspace. For more information about the format and configuration options available, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\">Working in your Grafana workspace</a>.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to update.</p>"""
    grafana_version: NotRequired["aws_sdk_grafana.types.grafana_version.GrafanaVersion"]
    """<p>Specifies the version of Grafana to support in the workspace. If not specified, keeps the current version of the workspace.</p> <p>Can only be used to upgrade (for example, from 8.4 to 9.4), not downgrade (for example, from 9.4 to 8.4).</p> <p>To know what versions are available to upgrade to for a specific workspace, see the <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html\">ListVersions</a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceConfigurationRequest) -> dict:
    out: dict = {}
    out["configuration"] = value["configuration"]
    if "grafana_version" in value:
        out["grafanaVersion"] = value["grafana_version"]
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceConfigurationRequest:
    out: UpdateWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        out["configuration"] = data["configuration"]
    else:
        raise DeserializationError(
            "UpdateWorkspaceConfigurationRequest.configuration required"
        )
    if "grafanaVersion" in data:
        out["grafana_version"] = data["grafanaVersion"]
    return out
