"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnTargetNetworksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.describe_client_vpn_target_networks_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.value_string_list


class DescribeClientVpnTargetNetworksRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    association_ids: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The IDs of the target network associations.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_client_vpn_target_networks_max_results.DescribeClientVpnTargetNetworksMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the nextToken value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p> <ul> <li> <p> <code>association-id</code> - The ID of the association.</p> </li> <li> <p> <code>target-network-id</code> - The ID of the subnet specified as the target network.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC in which the target network is located.</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClientVpnTargetNetworksRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "association_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["association_ids"], pairs, f"{prefix}.AssociationIds"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeClientVpnTargetNetworksRequest:
    out: DescribeClientVpnTargetNetworksRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    if el.find("AssociationIds") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["association_ids"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "AssociationIds"
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
