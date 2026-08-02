"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFlowLogsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.flow_log_id_list


class DeleteFlowLogsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    flow_log_ids: NotRequired["capo_ec2.types.flow_log_id_list.FlowLogIdList"]
    """<p>One or more flow log IDs.</p> <p>Constraint: Maximum of 1000 flow log IDs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteFlowLogsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "flow_log_ids" in value:
        import capo_ec2.types.flow_log_id_list

        capo_ec2.types.flow_log_id_list.serialize_ec2_query(
            value["flow_log_ids"], pairs, f"{key_prefix}FlowLogIds"
        )


def deserialize_ec2_query(el: Element) -> DeleteFlowLogsRequest:
    out: DeleteFlowLogsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("FlowLogIds") is not None:
        import capo_ec2.types.flow_log_id_list

        out["flow_log_ids"] = capo_ec2.types.flow_log_id_list.deserialize_ec2_query(
            el, "FlowLogIds"
        )
    return out
