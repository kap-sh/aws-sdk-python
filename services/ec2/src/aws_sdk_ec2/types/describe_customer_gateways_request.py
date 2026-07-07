"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCustomerGatewaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.customer_gateway_id_string_list
    import aws_sdk_ec2.types.filter_list


class DescribeCustomerGatewaysRequest(TypedDict, closed=True):
    customer_gateway_ids: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_id_string_list.CustomerGatewayIdStringList"
    ]
    """<p>One or more customer gateway IDs.</p> <p>Default: Describes all your customer gateways.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>bgp-asn</code> - The customer gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).</p> </li> <li> <p> <code>customer-gateway-id</code> - The ID of the customer gateway.</p> </li> <li> <p> <code>ip-address</code> - The IP address of the customer gateway device's external interface.</p> </li> <li> <p> <code>state</code> - The state of the customer gateway (<code>pending</code> | <code>available</code> | <code>deleting</code> | <code>deleted</code>).</p> </li> <li> <p> <code>type</code> - The type of customer gateway. Currently, the only supported type is <code>ipsec.1</code>.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCustomerGatewaysRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "customer_gateway_ids" in value:
        import aws_sdk_ec2.types.customer_gateway_id_string_list

        aws_sdk_ec2.types.customer_gateway_id_string_list.serialize_ec2_query(
            value["customer_gateway_ids"], pairs, f"{prefix}.CustomerGatewayIds"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeCustomerGatewaysRequest:
    out: DescribeCustomerGatewaysRequest = {}  # type: ignore[typeddict-item]
    if el.find("CustomerGatewayIds") is not None:
        import aws_sdk_ec2.types.customer_gateway_id_string_list

        out["customer_gateway_ids"] = (
            aws_sdk_ec2.types.customer_gateway_id_string_list.deserialize_ec2_query(
                el, "CustomerGatewayIds"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
