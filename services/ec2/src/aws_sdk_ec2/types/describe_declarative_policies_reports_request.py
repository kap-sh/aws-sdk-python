"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeDeclarativePoliciesReportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.declarative_policies_max_results
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class DescribeDeclarativePoliciesReportsRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.declarative_policies_max_results.DeclarativePoliciesMaxResults"
    ]
    r"""<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    report_ids: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>One or more report IDs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeDeclarativePoliciesReportsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "report_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["report_ids"], pairs, f"{prefix}.ReportIds"
        )


def deserialize_ec2_query(el: Element) -> DescribeDeclarativePoliciesReportsRequest:
    out: DescribeDeclarativePoliciesReportsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    if el.find("ReportIds") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["report_ids"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "ReportIds"
        )
    return out
