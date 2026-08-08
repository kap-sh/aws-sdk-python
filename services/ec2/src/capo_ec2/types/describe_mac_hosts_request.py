"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMacHostsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.describe_mac_hosts_request_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.request_host_id_list
    import capo_ec2.types.string


class DescribeMacHostsRequest(TypedDict, closed=True):
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone of the EC2 Mac Dedicated Host.</p> </li> <li> <p> <code>instance-type</code> - The instance type size that the EC2 Mac Dedicated Host is configured to support.</p> </li> </ul>"""
    host_ids: NotRequired["capo_ec2.types.request_host_id_list.RequestHostIdList"]
    """<p> The IDs of the EC2 Mac Dedicated Hosts. </p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_mac_hosts_request_max_results.DescribeMacHostsRequestMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value. This value can be between 5 and 500. If <code>maxResults</code> is given a larger value than 500, you receive an error.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeMacHostsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "host_ids" in value:
        import capo_ec2.types.request_host_id_list

        capo_ec2.types.request_host_id_list.serialize_ec2_query(
            value["host_ids"], pairs, f"{key_prefix}HostId"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeMacHostsRequest:
    out: DescribeMacHostsRequest = {}  # type: ignore[typeddict-item]
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    if el.find("HostId") is not None:
        import capo_ec2.types.request_host_id_list

        out["host_ids"] = capo_ec2.types.request_host_id_list.deserialize_ec2_query(
            el, "HostId"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
