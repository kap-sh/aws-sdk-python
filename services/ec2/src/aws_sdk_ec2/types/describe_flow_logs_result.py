"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFlowLogsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.flow_log_set
    import aws_sdk_ec2.types.string


class DescribeFlowLogsResult(TypedDict):
    flow_logs: NotRequired["aws_sdk_ec2.types.flow_log_set.FlowLogSet"]
    """<p>Information about the flow logs.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to request the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFlowLogsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "flow_logs" in value:
        import aws_sdk_ec2.types.flow_log_set

        aws_sdk_ec2.types.flow_log_set.serialize_ec2_query(
            value["flow_logs"], pairs, f"{prefix}.FlowLogSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeFlowLogsResult:
    out: DescribeFlowLogsResult = {}  # type: ignore[typeddict-item]
    if el.find("FlowLogSet") is not None:
        import aws_sdk_ec2.types.flow_log_set

        out["flow_logs"] = aws_sdk_ec2.types.flow_log_set.deserialize_ec2_query(
            el, "FlowLogSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
