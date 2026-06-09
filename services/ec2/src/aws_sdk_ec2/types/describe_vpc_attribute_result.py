"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_boolean_value
    import aws_sdk_ec2.types.string


class DescribeVpcAttributeResult(TypedDict):
    enable_dns_hostnames: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether the instances launched in the VPC get DNS hostnames. If this attribute is <code>true</code>, instances in the VPC get DNS hostnames; otherwise, they do not.</p>"""
    enable_dns_support: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether DNS resolution is enabled for the VPC. If this attribute is <code>true</code>, the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not.</p>"""
    enable_network_address_usage_metrics: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether Network Address Usage metrics are enabled for your VPC.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcAttributeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enable_dns_hostnames" in value:
        import aws_sdk_ec2.types.attribute_boolean_value

        aws_sdk_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_dns_hostnames"], pairs, f"{prefix}.EnableDnsHostnames"
        )
    if "enable_dns_support" in value:
        import aws_sdk_ec2.types.attribute_boolean_value

        aws_sdk_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_dns_support"], pairs, f"{prefix}.EnableDnsSupport"
        )
    if "enable_network_address_usage_metrics" in value:
        import aws_sdk_ec2.types.attribute_boolean_value

        aws_sdk_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["enable_network_address_usage_metrics"],
            pairs,
            f"{prefix}.EnableNetworkAddressUsageMetrics",
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcAttributeResult:
    out: DescribeVpcAttributeResult = {}  # type: ignore[typeddict-item]
    child_enable_dns_hostnames = el.find("EnableDnsHostnames")
    if child_enable_dns_hostnames is not None:
        import aws_sdk_ec2.types.attribute_boolean_value

        out["enable_dns_hostnames"] = (
            aws_sdk_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_dns_hostnames
            )
        )
    child_enable_dns_support = el.find("EnableDnsSupport")
    if child_enable_dns_support is not None:
        import aws_sdk_ec2.types.attribute_boolean_value

        out["enable_dns_support"] = (
            aws_sdk_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_dns_support
            )
        )
    child_enable_network_address_usage_metrics = el.find(
        "EnableNetworkAddressUsageMetrics"
    )
    if child_enable_network_address_usage_metrics is not None:
        import aws_sdk_ec2.types.attribute_boolean_value

        out["enable_network_address_usage_metrics"] = (
            aws_sdk_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_enable_network_address_usage_metrics
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
