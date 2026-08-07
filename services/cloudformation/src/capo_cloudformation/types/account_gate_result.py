"""Generated from Smithy shape ``com.amazonaws.cloudformation#AccountGateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.account_gate_status
    import capo_cloudformation.types.account_gate_status_reason


class AccountGateResult(TypedDict, closed=True):
    status: NotRequired[
        "capo_cloudformation.types.account_gate_status.AccountGateStatus"
    ]
    """<p>The status of the account gate function.</p> <ul> <li> <p> <code>SUCCEEDED</code>: The account gate function has determined that the account and Region passes any requirements for a StackSet operation to occur. CloudFormation proceeds with the stack operation in that account and Region.</p> </li> <li> <p> <code>FAILED</code>: The account gate function has determined that the account and Region doesn't meet the requirements for a StackSet operation to occur. CloudFormation cancels the StackSet operation in that account and Region, and sets the StackSet operation result status for that account and Region to <code>FAILED</code>.</p> </li> <li> <p> <code>SKIPPED</code>: CloudFormation has skipped calling the account gate function for this account and Region, for one of the following reasons:</p> <ul> <li> <p>An account gate function hasn't been specified for the account and Region. CloudFormation proceeds with the StackSet operation in this account and Region.</p> </li> <li> <p>The <code>AWSCloudFormationStackSetExecutionRole</code> of the administration account lacks permissions to invoke the function. CloudFormation proceeds with the StackSet operation in this account and Region.</p> </li> <li> <p>Either no action is necessary, or no action is possible, on the stack. CloudFormation skips the StackSet operation in this account and Region.</p> </li> </ul> </li> </ul>"""
    status_reason: NotRequired[
        "capo_cloudformation.types.account_gate_status_reason.AccountGateStatusReason"
    ]
    """<p>The reason for the account gate status assigned to this account and Region for the StackSet operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountGateResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_cloudformation.types.account_gate_status

        capo_cloudformation.types.account_gate_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_reason" in value:
        pairs.append((f"{key_prefix}StatusReason", str(value["status_reason"])))


def deserialize_query(el: Element) -> AccountGateResult:
    out: AccountGateResult = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.account_gate_status

        out["status"] = capo_cloudformation.types.account_gate_status.deserialize_query(
            child_status
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    return out
