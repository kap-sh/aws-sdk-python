"""Generated from Smithy shape ``com.amazonaws.grafana#DescribeWorkspaceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.grafana_version
    import aws_sdk_grafana.types.overridable_configuration_json


class DescribeWorkspaceConfigurationResponse(TypedDict, closed=True):
    configuration: "aws_sdk_grafana.types.overridable_configuration_json.OverridableConfigurationJson"
    r"""<p>The configuration string for the workspace that you requested. For more information about the format and configuration options available, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\">Working in your Grafana workspace</a>.</p>"""
    grafana_version: NotRequired["aws_sdk_grafana.types.grafana_version.GrafanaVersion"]
    """<p>The supported Grafana version for the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceConfigurationResponse) -> dict:
    out: dict = {}
    out["configuration"] = value["configuration"]
    if "grafana_version" in value:
        out["grafanaVersion"] = value["grafana_version"]
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceConfigurationResponse:
    out: DescribeWorkspaceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        out["configuration"] = data["configuration"]
    else:
        raise DeserializationError(
            "DescribeWorkspaceConfigurationResponse.configuration required"
        )
    if "grafanaVersion" in data:
        out["grafana_version"] = data["grafanaVersion"]
    return out
