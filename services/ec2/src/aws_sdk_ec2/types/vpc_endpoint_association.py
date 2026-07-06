"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dns_entry
    import aws_sdk_ec2.types.service_network_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_endpoint_id


class VpcEndpointAssociation(TypedDict, closed=True):
    id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC endpoint association.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of the VPC endpoint.</p>"""
    service_network_arn: NotRequired[
        "aws_sdk_ec2.types.service_network_arn.ServiceNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    service_network_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the service network.</p>"""
    associated_resource_accessibility: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The connectivity status of the resources associated to a VPC endpoint. The resource is accessible if the associated resource configuration is <code>AVAILABLE</code>, otherwise the resource is inaccessible.</p>"""
    failure_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message related to why an VPC endpoint association failed.</p>"""
    failure_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An error code related to why an VPC endpoint association failed.</p>"""
    dns_entry: NotRequired["aws_sdk_ec2.types.dns_entry.DnsEntry"]
    """<p>The DNS entry of the VPC endpoint association.</p>"""
    private_dns_entry: NotRequired["aws_sdk_ec2.types.dns_entry.DnsEntry"]
    """<p>The private DNS entry of the VPC endpoint association.</p>"""
    associated_resource_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the associated resource.</p>"""
    resource_configuration_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource configuration group.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags to apply to the VPC endpoint association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEndpointAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "vpc_endpoint_id" in value:
        pairs.append((f"{prefix}.VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "service_network_arn" in value:
        pairs.append((f"{prefix}.ServiceNetworkArn", str(value["service_network_arn"])))
    if "service_network_name" in value:
        pairs.append(
            (f"{prefix}.ServiceNetworkName", str(value["service_network_name"]))
        )
    if "associated_resource_accessibility" in value:
        pairs.append(
            (
                f"{prefix}.AssociatedResourceAccessibility",
                str(value["associated_resource_accessibility"]),
            )
        )
    if "failure_reason" in value:
        pairs.append((f"{prefix}.FailureReason", str(value["failure_reason"])))
    if "failure_code" in value:
        pairs.append((f"{prefix}.FailureCode", str(value["failure_code"])))
    if "dns_entry" in value:
        import aws_sdk_ec2.types.dns_entry

        aws_sdk_ec2.types.dns_entry.serialize_ec2_query(
            value["dns_entry"], pairs, f"{prefix}.DnsEntry"
        )
    if "private_dns_entry" in value:
        import aws_sdk_ec2.types.dns_entry

        aws_sdk_ec2.types.dns_entry.serialize_ec2_query(
            value["private_dns_entry"], pairs, f"{prefix}.PrivateDnsEntry"
        )
    if "associated_resource_arn" in value:
        pairs.append(
            (f"{prefix}.AssociatedResourceArn", str(value["associated_resource_arn"]))
        )
    if "resource_configuration_group_arn" in value:
        pairs.append(
            (
                f"{prefix}.ResourceConfigurationGroupArn",
                str(value["resource_configuration_group_arn"]),
            )
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> VpcEndpointAssociation:
    out: VpcEndpointAssociation = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_service_network_arn = el.find("ServiceNetworkArn")
    if child_service_network_arn is not None:
        out["service_network_arn"] = str(child_service_network_arn.text or "")
    child_service_network_name = el.find("ServiceNetworkName")
    if child_service_network_name is not None:
        out["service_network_name"] = str(child_service_network_name.text or "")
    child_associated_resource_accessibility = el.find("AssociatedResourceAccessibility")
    if child_associated_resource_accessibility is not None:
        out["associated_resource_accessibility"] = str(
            child_associated_resource_accessibility.text or ""
        )
    child_failure_reason = el.find("FailureReason")
    if child_failure_reason is not None:
        out["failure_reason"] = str(child_failure_reason.text or "")
    child_failure_code = el.find("FailureCode")
    if child_failure_code is not None:
        out["failure_code"] = str(child_failure_code.text or "")
    child_dns_entry = el.find("DnsEntry")
    if child_dns_entry is not None:
        import aws_sdk_ec2.types.dns_entry

        out["dns_entry"] = aws_sdk_ec2.types.dns_entry.deserialize_ec2_query(
            child_dns_entry
        )
    child_private_dns_entry = el.find("PrivateDnsEntry")
    if child_private_dns_entry is not None:
        import aws_sdk_ec2.types.dns_entry

        out["private_dns_entry"] = aws_sdk_ec2.types.dns_entry.deserialize_ec2_query(
            child_private_dns_entry
        )
    child_associated_resource_arn = el.find("AssociatedResourceArn")
    if child_associated_resource_arn is not None:
        out["associated_resource_arn"] = str(child_associated_resource_arn.text or "")
    child_resource_configuration_group_arn = el.find("ResourceConfigurationGroupArn")
    if child_resource_configuration_group_arn is not None:
        out["resource_configuration_group_arn"] = str(
            child_resource_configuration_group_arn.text or ""
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
