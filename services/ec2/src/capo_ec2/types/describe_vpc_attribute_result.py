"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcAttributeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_boolean_value
    import capo_ec2.types.string


class DescribeVpcAttributeResult(TypedDict, closed=True):
    enable_dns_hostnames: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether the instances launched in the VPC get DNS hostnames. If this attribute is <code>true</code>, instances in the VPC get DNS hostnames; otherwise, they do not.</p>"""
    enable_dns_support: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether DNS resolution is enabled for the VPC. If this attribute is <code>true</code>, the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not.</p>"""
    enable_network_address_usage_metrics: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether Network Address Usage metrics are enabled for your VPC.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcAttributeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enable_dns_hostnames" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_dns_hostnames"], pairs, f"{key_prefix}EnableDnsHostnames"
        )
    if "enable_dns_support" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_dns_support"], pairs, f"{key_prefix}EnableDnsSupport"
        )
    if "enable_network_address_usage_metrics" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_network_address_usage_metrics"],
            pairs,
            f"{key_prefix}EnableNetworkAddressUsageMetrics",
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcAttributeResult:
    out: DescribeVpcAttributeResult = {}  # type: ignore[typeddict-item]
    child_enable_dns_hostnames = el.find("enableDnsHostnames")
    if child_enable_dns_hostnames is not None:
        import capo_ec2.types.attribute_boolean_value

        out["enable_dns_hostnames"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_dns_hostnames
            )
        )
    child_enable_dns_support = el.find("enableDnsSupport")
    if child_enable_dns_support is not None:
        import capo_ec2.types.attribute_boolean_value

        out["enable_dns_support"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_dns_support
            )
        )
    child_enable_network_address_usage_metrics = el.find(
        "enableNetworkAddressUsageMetrics"
    )
    if child_enable_network_address_usage_metrics is not None:
        import capo_ec2.types.attribute_boolean_value

        out["enable_network_address_usage_metrics"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_network_address_usage_metrics
            )
        )
    child_vpc_id = el.find("vpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
