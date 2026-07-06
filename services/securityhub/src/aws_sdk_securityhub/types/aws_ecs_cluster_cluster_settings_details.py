"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterClusterSettingsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsClusterClusterSettingsDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the setting. The valid value is <code>containerInsights</code>.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of the setting. Valid values are <code>disabled</code> or <code>enabled</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsClusterClusterSettingsDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsEcsClusterClusterSettingsDetails:
    out: AwsEcsClusterClusterSettingsDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
