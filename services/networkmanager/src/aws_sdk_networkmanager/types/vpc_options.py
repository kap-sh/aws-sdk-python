"""Generated from Smithy shape ``com.amazonaws.networkmanager#VpcOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.boolean


class VpcOptions(TypedDict, closed=True):
    ipv6_support: "aws_sdk_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether IPv6 is supported.</p>"""
    appliance_mode_support: "aws_sdk_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether appliance mode is supported. If enabled, traffic flow between a source and destination use the same Availability Zone for the VPC attachment for the lifetime of that flow. The default value is <code>false</code>.</p>"""
    dns_support: "aws_sdk_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether DNS is supported.</p>"""
    security_group_referencing_support: "aws_sdk_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether security group referencing is enabled for this VPC attachment. The default is <code>true</code>. However, at the core network policy-level the default is set to <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcOptions) -> dict:
    out: dict = {}
    out["Ipv6Support"] = value.get("ipv6_support", False)
    out["ApplianceModeSupport"] = value.get("appliance_mode_support", False)
    out["DnsSupport"] = value.get("dns_support", False)
    out["SecurityGroupReferencingSupport"] = value.get(
        "security_group_referencing_support", False
    )
    return out


def deserialize_json(data: dict) -> VpcOptions:
    out: VpcOptions = {}  # type: ignore[typeddict-item]
    if "Ipv6Support" in data:
        out["ipv6_support"] = data["Ipv6Support"]
    else:
        out["ipv6_support"] = False
    if "ApplianceModeSupport" in data:
        out["appliance_mode_support"] = data["ApplianceModeSupport"]
    else:
        out["appliance_mode_support"] = False
    if "DnsSupport" in data:
        out["dns_support"] = data["DnsSupport"]
    else:
        out["dns_support"] = False
    if "SecurityGroupReferencingSupport" in data:
        out["security_group_referencing_support"] = data[
            "SecurityGroupReferencingSupport"
        ]
    else:
        out["security_group_referencing_support"] = False
    return out
