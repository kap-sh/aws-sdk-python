"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnAuthorizationRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.describe_client_vpn_authorization_rules_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token


class DescribeClientVpnAuthorizationRulesRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p> <ul> <li> <p> <code>description</code> - The description of the authorization rule.</p> </li> <li> <p> <code>destination-cidr</code> - The CIDR of the network to which the authorization rule applies.</p> </li> <li> <p> <code>group-id</code> - The ID of the Active Directory group to which the authorization rule grants access.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_client_vpn_authorization_rules_max_results.DescribeClientVpnAuthorizationRulesMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the nextToken value.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClientVpnAuthorizationRulesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeClientVpnAuthorizationRulesRequest:
    out: DescribeClientVpnAuthorizationRulesRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
