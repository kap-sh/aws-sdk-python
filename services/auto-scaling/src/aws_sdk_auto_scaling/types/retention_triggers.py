"""Generated from Smithy shape ``com.amazonaws.autoscaling#RetentionTriggers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.retention_action


class RetentionTriggers(TypedDict, closed=True):
    terminate_hook_abandon: NotRequired[
        "aws_sdk_auto_scaling.types.retention_action.RetentionAction"
    ]
    """<p> Specifies the action when a termination lifecycle hook is abandoned due to failure, timeout, or explicit abandonment (calling CompleteLifecycleAction). </p> <p> Set to <code>retain</code> to move instances to a retained state. Set to <code>terminate</code> for default termination behavior. </p> <p> Retained instances don't count toward desired capacity and remain until you call <code>TerminateInstanceInAutoScalingGroup</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RetentionTriggers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "terminate_hook_abandon" in value:
        import aws_sdk_auto_scaling.types.retention_action

        aws_sdk_auto_scaling.types.retention_action.serialize_query(
            value["terminate_hook_abandon"], pairs, f"{prefix}.TerminateHookAbandon"
        )


def deserialize_query(el: Element) -> RetentionTriggers:
    out: RetentionTriggers = {}  # type: ignore[typeddict-item]
    child_terminate_hook_abandon = el.find("TerminateHookAbandon")
    if child_terminate_hook_abandon is not None:
        import aws_sdk_auto_scaling.types.retention_action

        out["terminate_hook_abandon"] = (
            aws_sdk_auto_scaling.types.retention_action.deserialize_query(
                child_terminate_hook_abandon
            )
        )
    return out
