"""Generated from Smithy shape ``com.amazonaws.autoscaling#RetentionTriggers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.retention_action


class RetentionTriggers(TypedDict, closed=True):
    terminate_hook_abandon: NotRequired[
        "capo_auto_scaling.types.retention_action.RetentionAction"
    ]
    """<p> Specifies the action when a termination lifecycle hook is abandoned due to failure, timeout, or explicit abandonment (calling CompleteLifecycleAction). </p> <p> Set to <code>retain</code> to move instances to a retained state. Set to <code>terminate</code> for default termination behavior. </p> <p> Retained instances don't count toward desired capacity and remain until you call <code>TerminateInstanceInAutoScalingGroup</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RetentionTriggers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "terminate_hook_abandon" in value:
        import capo_auto_scaling.types.retention_action

        capo_auto_scaling.types.retention_action.serialize_query(
            value["terminate_hook_abandon"], pairs, f"{key_prefix}TerminateHookAbandon"
        )


def deserialize_query(el: Element) -> RetentionTriggers:
    out: RetentionTriggers = {}  # type: ignore[typeddict-item]
    child_terminate_hook_abandon = el.find("TerminateHookAbandon")
    if child_terminate_hook_abandon is not None:
        import capo_auto_scaling.types.retention_action

        out["terminate_hook_abandon"] = (
            capo_auto_scaling.types.retention_action.deserialize_query(
                child_terminate_hook_abandon
            )
        )
    return out
