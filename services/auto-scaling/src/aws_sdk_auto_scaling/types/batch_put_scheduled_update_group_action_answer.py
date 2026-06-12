"""Generated from Smithy shape ``com.amazonaws.autoscaling#BatchPutScheduledUpdateGroupActionAnswer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.failed_scheduled_update_group_action_requests


class BatchPutScheduledUpdateGroupActionAnswer(TypedDict):
    failed_scheduled_update_group_actions: NotRequired[
        "aws_sdk_auto_scaling.types.failed_scheduled_update_group_action_requests.FailedScheduledUpdateGroupActionRequests"
    ]
    """<p>The names of the scheduled actions that could not be created or updated, including an error message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchPutScheduledUpdateGroupActionAnswer,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "failed_scheduled_update_group_actions" in value:
        import aws_sdk_auto_scaling.types.failed_scheduled_update_group_action_requests

        aws_sdk_auto_scaling.types.failed_scheduled_update_group_action_requests.serialize_query(
            value["failed_scheduled_update_group_actions"],
            pairs,
            f"{prefix}.FailedScheduledUpdateGroupActions",
        )


def deserialize_query(el: Element) -> BatchPutScheduledUpdateGroupActionAnswer:
    out: BatchPutScheduledUpdateGroupActionAnswer = {}  # type: ignore[typeddict-item]
    child_failed_scheduled_update_group_actions = el.find(
        "FailedScheduledUpdateGroupActions"
    )
    if child_failed_scheduled_update_group_actions is not None:
        import aws_sdk_auto_scaling.types.failed_scheduled_update_group_action_requests

        out["failed_scheduled_update_group_actions"] = (
            aws_sdk_auto_scaling.types.failed_scheduled_update_group_action_requests.deserialize_query(
                child_failed_scheduled_update_group_actions
            )
        )
    return out
