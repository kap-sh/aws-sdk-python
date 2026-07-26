"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataEnclaveOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class AwsEc2LaunchTemplateDataEnclaveOptionsDetails(TypedDict, closed=True):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> If this parameter is set to <code>true</code>, the instance is enabled for Amazon Web Services Nitro Enclaves. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataEnclaveOptionsDetails) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataEnclaveOptionsDetails:
    out: AwsEc2LaunchTemplateDataEnclaveOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
