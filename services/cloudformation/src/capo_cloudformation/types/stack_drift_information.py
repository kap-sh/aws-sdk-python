"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackDriftInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stack_drift_status
    import capo_cloudformation.types.timestamp


class StackDriftInformation(TypedDict, closed=True):
    stack_drift_status: NotRequired[
        "capo_cloudformation.types.stack_drift_status.StackDriftStatus"
    ]
    """<p>Status of the stack's actual configuration compared to its expected template configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked if the stack differs from its expected template configuration.</p> </li> <li> <p> <code>IN_SYNC</code>: The stack's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: CloudFormation could not run drift detection for a resource in the stack.</p> </li> </ul>"""
    last_check_timestamp: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackDriftInformation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_drift_status" in value:
        import capo_cloudformation.types.stack_drift_status

        capo_cloudformation.types.stack_drift_status.serialize_query(
            value["stack_drift_status"], pairs, f"{key_prefix}StackDriftStatus"
        )
    if "last_check_timestamp" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["last_check_timestamp"], pairs, f"{key_prefix}LastCheckTimestamp"
        )


def deserialize_query(el: Element) -> StackDriftInformation:
    out: StackDriftInformation = {}  # type: ignore[typeddict-item]
    child_stack_drift_status = el.find("StackDriftStatus")
    if child_stack_drift_status is not None:
        import capo_cloudformation.types.stack_drift_status

        out["stack_drift_status"] = (
            capo_cloudformation.types.stack_drift_status.deserialize_query(
                child_stack_drift_status
            )
        )
    child_last_check_timestamp = el.find("LastCheckTimestamp")
    if child_last_check_timestamp is not None:
        import capo_cloudformation.types.timestamp

        out["last_check_timestamp"] = (
            capo_cloudformation.types.timestamp.deserialize_query(
                child_last_check_timestamp
            )
        )
    return out
