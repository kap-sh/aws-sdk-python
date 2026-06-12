"""Generated from Smithy shape ``com.amazonaws.fms#FMSPolicyUpdateFirewallCreationConfigAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.managed_service_data


class FMSPolicyUpdateFirewallCreationConfigAction(TypedDict):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>Describes the remedial action.</p>"""
    firewall_creation_config: NotRequired[
        "aws_sdk_fms.types.managed_service_data.ManagedServiceData"
    ]
    """<p>A <code>FirewallCreationConfig</code> that you can copy into your current policy's <a href=\"https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html\">SecurityServiceData</a> in order to remedy scope violations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FMSPolicyUpdateFirewallCreationConfigAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "firewall_creation_config" in value:
        out["FirewallCreationConfig"] = value["firewall_creation_config"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FMSPolicyUpdateFirewallCreationConfigAction:
    out: FMSPolicyUpdateFirewallCreationConfigAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "FirewallCreationConfig" in data:
        out["firewall_creation_config"] = data["FirewallCreationConfig"]
    return out
