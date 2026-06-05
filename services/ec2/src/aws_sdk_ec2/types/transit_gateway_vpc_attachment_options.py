"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayVpcAttachmentOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.appliance_mode_support_value
    import aws_sdk_ec2.types.dns_support_value
    import aws_sdk_ec2.types.ipv6_support_value
    import aws_sdk_ec2.types.security_group_referencing_support_value


class TransitGatewayVpcAttachmentOptions(TypedDict):
    dns_support: NotRequired["aws_sdk_ec2.types.dns_support_value.DnsSupportValue"]
    """<p>Indicates whether DNS support is enabled.</p>"""
    security_group_referencing_support: NotRequired[
        "aws_sdk_ec2.types.security_group_referencing_support_value.SecurityGroupReferencingSupportValue"
    ]
    """<p>Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.</p> <p>This option is enabled by default.</p> <p>For more information about security group referencing, see <a href=\"https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security\">Security group referencing</a> in the <i>Amazon Web Services Transit Gateways Guide</i>.</p>"""
    ipv6_support: NotRequired["aws_sdk_ec2.types.ipv6_support_value.Ipv6SupportValue"]
    """<p>Indicates whether IPv6 support is disabled.</p>"""
    appliance_mode_support: NotRequired[
        "aws_sdk_ec2.types.appliance_mode_support_value.ApplianceModeSupportValue"
    ]
    """<p>Indicates whether appliance mode support is enabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayVpcAttachmentOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dns_support" in value:
        import aws_sdk_ec2.types.dns_support_value

        aws_sdk_ec2.types.dns_support_value.serialize_ec2_query(
            value["dns_support"], pairs, f"{prefix}.DnsSupport"
        )
    if "security_group_referencing_support" in value:
        import aws_sdk_ec2.types.security_group_referencing_support_value

        aws_sdk_ec2.types.security_group_referencing_support_value.serialize_ec2_query(
            value["security_group_referencing_support"],
            pairs,
            f"{prefix}.SecurityGroupReferencingSupport",
        )
    if "ipv6_support" in value:
        import aws_sdk_ec2.types.ipv6_support_value

        aws_sdk_ec2.types.ipv6_support_value.serialize_ec2_query(
            value["ipv6_support"], pairs, f"{prefix}.Ipv6Support"
        )
    if "appliance_mode_support" in value:
        import aws_sdk_ec2.types.appliance_mode_support_value

        aws_sdk_ec2.types.appliance_mode_support_value.serialize_ec2_query(
            value["appliance_mode_support"], pairs, f"{prefix}.ApplianceModeSupport"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayVpcAttachmentOptions:
    out: TransitGatewayVpcAttachmentOptions = {}  # type: ignore[typeddict-item]
    child_dns_support = el.find("DnsSupport")
    if child_dns_support is not None:
        import aws_sdk_ec2.types.dns_support_value

        out["dns_support"] = aws_sdk_ec2.types.dns_support_value.deserialize_ec2_query(
            child_dns_support
        )
    child_security_group_referencing_support = el.find(
        "SecurityGroupReferencingSupport"
    )
    if child_security_group_referencing_support is not None:
        import aws_sdk_ec2.types.security_group_referencing_support_value

        out["security_group_referencing_support"] = (
            aws_sdk_ec2.types.security_group_referencing_support_value.deserialize_ec2_query(
                child_security_group_referencing_support
            )
        )
    child_ipv6_support = el.find("Ipv6Support")
    if child_ipv6_support is not None:
        import aws_sdk_ec2.types.ipv6_support_value

        out["ipv6_support"] = (
            aws_sdk_ec2.types.ipv6_support_value.deserialize_ec2_query(
                child_ipv6_support
            )
        )
    child_appliance_mode_support = el.find("ApplianceModeSupport")
    if child_appliance_mode_support is not None:
        import aws_sdk_ec2.types.appliance_mode_support_value

        out["appliance_mode_support"] = (
            aws_sdk_ec2.types.appliance_mode_support_value.deserialize_ec2_query(
                child_appliance_mode_support
            )
        )
    return out
