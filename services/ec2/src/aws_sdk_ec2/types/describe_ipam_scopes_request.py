"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamScopesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.ipam_max_results
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.value_string_list


class DescribeIpamScopesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters for the request. For more information about filtering, see <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html\">Filtering CLI output</a>.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    ipam_scope_ids: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The IDs of the scopes you want information on.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamScopesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "ipam_scope_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["ipam_scope_ids"], pairs, f"{prefix}.IpamScopeIds"
        )


def deserialize_ec2_query(el: Element) -> DescribeIpamScopesRequest:
    out: DescribeIpamScopesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("IpamScopeIds") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["ipam_scope_ids"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "IpamScopeIds"
            )
        )
    return out
