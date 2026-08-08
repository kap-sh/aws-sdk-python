"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFlowLogsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flow_log_set
    import capo_ec2.types.string


class DescribeFlowLogsResult(TypedDict, closed=True):
    flow_logs: NotRequired["capo_ec2.types.flow_log_set.FlowLogSet"]
    """<p>Information about the flow logs.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to request the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFlowLogsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "flow_logs" in value:
        import capo_ec2.types.flow_log_set

        capo_ec2.types.flow_log_set.serialize_ec2_query(
            value["flow_logs"], pairs, f"{key_prefix}FlowLogSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeFlowLogsResult:
    out: DescribeFlowLogsResult = {}  # type: ignore[typeddict-item]
    if el.find("flowLogSet") is not None:
        import capo_ec2.types.flow_log_set

        out["flow_logs"] = capo_ec2.types.flow_log_set.deserialize_ec2_query(
            el, "flowLogSet"
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
