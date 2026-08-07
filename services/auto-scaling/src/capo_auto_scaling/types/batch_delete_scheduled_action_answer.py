"""Generated from Smithy shape ``com.amazonaws.autoscaling#BatchDeleteScheduledActionAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.failed_scheduled_update_group_action_requests


class BatchDeleteScheduledActionAnswer(TypedDict, closed=True):
    failed_scheduled_actions: NotRequired[
        "capo_auto_scaling.types.failed_scheduled_update_group_action_requests.FailedScheduledUpdateGroupActionRequests"
    ]
    """<p>The names of the scheduled actions that could not be deleted, including an error message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchDeleteScheduledActionAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "failed_scheduled_actions" in value:
        import capo_auto_scaling.types.failed_scheduled_update_group_action_requests

        capo_auto_scaling.types.failed_scheduled_update_group_action_requests.serialize_query(
            value["failed_scheduled_actions"],
            pairs,
            f"{key_prefix}FailedScheduledActions",
        )


def deserialize_query(el: Element) -> BatchDeleteScheduledActionAnswer:
    out: BatchDeleteScheduledActionAnswer = {}  # type: ignore[typeddict-item]
    child_failed_scheduled_actions = el.find("FailedScheduledActions")
    if child_failed_scheduled_actions is not None:
        import capo_auto_scaling.types.failed_scheduled_update_group_action_requests

        out["failed_scheduled_actions"] = (
            capo_auto_scaling.types.failed_scheduled_update_group_action_requests.deserialize_query(
                child_failed_scheduled_actions
            )
        )
    return out
