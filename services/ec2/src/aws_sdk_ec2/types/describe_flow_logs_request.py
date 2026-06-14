"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFlowLogsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.flow_log_id_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeFlowLogsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filter: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>deliver-log-status</code> - The status of the logs delivery (<code>SUCCESS</code> | <code>FAILED</code>).</p> </li> <li> <p> <code>log-destination-type</code> - The type of destination for the flow log data (<code>cloud-watch-logs</code> | <code>s3</code> | <code>kinesis-data-firehose</code>).</p> </li> <li> <p> <code>flow-log-id</code> - The ID of the flow log.</p> </li> <li> <p> <code>log-group-name</code> - The name of the log group.</p> </li> <li> <p> <code>resource-id</code> - The ID of the VPC, subnet, or network interface.</p> </li> <li> <p> <code>traffic-type</code> - The type of traffic (<code>ACCEPT</code> | <code>REJECT</code> | <code>ALL</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    flow_log_ids: NotRequired["aws_sdk_ec2.types.flow_log_id_list.FlowLogIdList"]
    """<p>One or more flow log IDs.</p> <p>Constraint: Maximum of 1000 flow log IDs.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    r"""<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to request the next page of items. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFlowLogsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filter" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filter"], pairs, f"{prefix}.Filter"
        )
    if "flow_log_ids" in value:
        import aws_sdk_ec2.types.flow_log_id_list

        aws_sdk_ec2.types.flow_log_id_list.serialize_ec2_query(
            value["flow_log_ids"], pairs, f"{prefix}.FlowLogIds"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeFlowLogsRequest:
    out: DescribeFlowLogsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filter") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filter"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filter"
        )
    if el.find("FlowLogIds") is not None:
        import aws_sdk_ec2.types.flow_log_id_list

        out["flow_log_ids"] = aws_sdk_ec2.types.flow_log_id_list.deserialize_ec2_query(
            el, "FlowLogIds"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
