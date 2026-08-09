"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondarySubnetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_secondary_subnets_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.secondary_subnet_id_list
    import capo_ec2.types.string


class DescribeSecondarySubnetsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>ipv4-cidr-block-association.association-id</code> - The association ID for an IPv4 CIDR block associated with the secondary subnet.</p> </li> <li> <p> <code>ipv4-cidr-block-association.cidr-block</code> - An IPv4 CIDR block associated with the secondary subnet.</p> </li> <li> <p> <code>ipv4-cidr-block-association.state</code> - The state of an IPv4 CIDR block associated with the secondary subnet.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the secondary subnet.</p> </li> <li> <p> <code>secondary-network-id</code> - The ID of the secondary network.</p> </li> <li> <p> <code>secondary-network-type</code> - The type of the secondary network (<code>rdma</code>).</p> </li> <li> <p> <code>secondary-subnet-id</code> - The ID of the secondary subnet.</p> </li> <li> <p> <code>secondary-subnet-arn</code> - The ARN of the secondary subnet.</p> </li> <li> <p> <code>state</code> - The state of the secondary subnet (<code>create-in-progress</code> | <code>create-complete</code> | <code>create-failed</code> | <code>delete-in-progress</code> | <code>delete-complete</code> | <code>delete-failed</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_secondary_subnets_max_results.DescribeSecondarySubnetsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    secondary_subnet_ids: NotRequired[
        "capo_ec2.types.secondary_subnet_id_list.SecondarySubnetIdList"
    ]
    """<p>The IDs of the secondary subnets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecondarySubnetsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "secondary_subnet_ids" in value:
        import capo_ec2.types.secondary_subnet_id_list

        capo_ec2.types.secondary_subnet_id_list.serialize_ec2_query(
            value["secondary_subnet_ids"], pairs, f"{key_prefix}SecondarySubnetId"
        )


def deserialize_ec2_query(el: Element) -> DescribeSecondarySubnetsRequest:
    out: DescribeSecondarySubnetsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_secondary_subnet_ids = el.find("SecondarySubnetId")
    if child_secondary_subnet_ids is not None:
        import capo_ec2.types.secondary_subnet_id_list

        out["secondary_subnet_ids"] = (
            capo_ec2.types.secondary_subnet_id_list.deserialize_ec2_query(
                child_secondary_subnet_ids
            )
        )
    return out
