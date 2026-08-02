"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMovingAddressesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_moving_addresses_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class DescribeMovingAddressesRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    public_ips: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>One or more Elastic IP addresses.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>moving-status</code> - The status of the Elastic IP address (<code>MovingToVpc</code> | <code>RestoringToClassic</code>).</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_moving_addresses_max_results.DescribeMovingAddressesMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned <code>NextToken</code> value. This value can be between 5 and 1000; if <code>MaxResults</code> is given a value outside of this range, an error is returned.</p> <p>Default: If no value is provided, the default is 1000.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeMovingAddressesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "public_ips" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["public_ips"], pairs, f"{key_prefix}PublicIp"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeMovingAddressesRequest:
    out: DescribeMovingAddressesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("PublicIp") is not None:
        import capo_ec2.types.value_string_list

        out["public_ips"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "PublicIp"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
