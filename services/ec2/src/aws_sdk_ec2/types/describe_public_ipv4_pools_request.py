"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePublicIpv4PoolsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.pool_max_results
    import aws_sdk_ec2.types.public_ipv4_pool_id_string_list


class DescribePublicIpv4PoolsRequest(TypedDict):
    pool_ids: NotRequired[
        "aws_sdk_ec2.types.public_ipv4_pool_id_string_list.PublicIpv4PoolIdStringList"
    ]
    """<p>The IDs of the address pools.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.pool_max_results.PoolMaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribePublicIpv4PoolsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "pool_ids" in value:
        import aws_sdk_ec2.types.public_ipv4_pool_id_string_list

        aws_sdk_ec2.types.public_ipv4_pool_id_string_list.serialize_ec2_query(
            value["pool_ids"], pairs, f"{prefix}.PoolIds"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_ec2_query(el: Element) -> DescribePublicIpv4PoolsRequest:
    out: DescribePublicIpv4PoolsRequest = {}  # type: ignore[typeddict-item]
    if el.find("PoolIds") is not None:
        import aws_sdk_ec2.types.public_ipv4_pool_id_string_list

        out["pool_ids"] = (
            aws_sdk_ec2.types.public_ipv4_pool_id_string_list.deserialize_ec2_query(
                el, "PoolIds"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    return out
