"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails(
    TypedDict, closed=True
):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>If set to <code>true</code>, then instances in the group launch with detailed monitoring.</p> <p>If set to <code>false</code>, then instances in the group launch with basic monitoring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails,
) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(
    data: dict,
) -> AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails:
    out: AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
