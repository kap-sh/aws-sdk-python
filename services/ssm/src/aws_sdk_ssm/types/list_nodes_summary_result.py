"""Generated from Smithy shape ``com.amazonaws.ssm#ListNodesSummaryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.node_summary_list


class ListNodesSummaryResult(TypedDict, closed=True):
    summary: NotRequired["aws_sdk_ssm.types.node_summary_list.NodeSummaryList"]
    """<p>A collection of objects reporting information about your managed nodes, such as the count of nodes by operating system.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNodesSummaryResult) -> dict:
    out: dict = {}
    if "summary" in value:
        import aws_sdk_ssm.types.node_summary_list

        out["Summary"] = aws_sdk_ssm.types.node_summary_list.serialize_aws_json_1_1(
            value["summary"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNodesSummaryResult:
    out: ListNodesSummaryResult = {}  # type: ignore[typeddict-item]
    if "Summary" in data:
        import aws_sdk_ssm.types.node_summary_list

        out["summary"] = aws_sdk_ssm.types.node_summary_list.deserialize_aws_json_1_1(
            data["Summary"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
