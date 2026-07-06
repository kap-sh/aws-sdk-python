"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointServiceConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.value_string_list


class CreateVpcEndpointServiceConfigurationRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    acceptance_required: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether requests from service consumers to create an endpoint to your service must be accepted manually.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>(Interface endpoint configuration) The private DNS name to assign to the VPC endpoint service.</p>"""
    network_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Network Load Balancers.</p>"""
    gateway_load_balancer_arns: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Gateway Load Balancers.</p>"""
    supported_ip_address_types: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The supported IP address types. The possible values are <code>ipv4</code> and <code>ipv6</code>.</p>"""
    supported_regions: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The Regions from which service consumers can access the service.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to associate with the service.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcEndpointServiceConfigurationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "acceptance_required" in value:
        pairs.append(
            (
                f"{prefix}.AcceptanceRequired",
                "true" if value["acceptance_required"] else "false",
            )
        )
    if "private_dns_name" in value:
        pairs.append((f"{prefix}.PrivateDnsName", str(value["private_dns_name"])))
    if "network_load_balancer_arns" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["network_load_balancer_arns"],
            pairs,
            f"{prefix}.NetworkLoadBalancerArns",
        )
    if "gateway_load_balancer_arns" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["gateway_load_balancer_arns"],
            pairs,
            f"{prefix}.GatewayLoadBalancerArns",
        )
    if "supported_ip_address_types" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["supported_ip_address_types"],
            pairs,
            f"{prefix}.SupportedIpAddressTypes",
        )
    if "supported_regions" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["supported_regions"], pairs, f"{prefix}.SupportedRegions"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> CreateVpcEndpointServiceConfigurationRequest:
    out: CreateVpcEndpointServiceConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_acceptance_required = el.find("AcceptanceRequired")
    if child_acceptance_required is not None:
        out["acceptance_required"] = (
            child_acceptance_required.text or ""
        ).lower() == "true"
    child_private_dns_name = el.find("PrivateDnsName")
    if child_private_dns_name is not None:
        out["private_dns_name"] = str(child_private_dns_name.text or "")
    if el.find("NetworkLoadBalancerArns") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["network_load_balancer_arns"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "NetworkLoadBalancerArns"
            )
        )
    if el.find("GatewayLoadBalancerArns") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["gateway_load_balancer_arns"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "GatewayLoadBalancerArns"
            )
        )
    if el.find("SupportedIpAddressTypes") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["supported_ip_address_types"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "SupportedIpAddressTypes"
            )
        )
    if el.find("SupportedRegions") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["supported_regions"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "SupportedRegions"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
