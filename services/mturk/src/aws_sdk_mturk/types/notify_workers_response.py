"""Generated from Smithy shape ``com.amazonaws.mturk#NotifyWorkersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.notify_workers_failure_status_list


class NotifyWorkersResponse(TypedDict):
    notify_workers_failure_statuses: NotRequired[
        "aws_sdk_mturk.types.notify_workers_failure_status_list.NotifyWorkersFailureStatusList"
    ]
    """<p> When MTurk sends notifications to the list of Workers, it returns back any failures it encounters in this list of NotifyWorkersFailureStatus objects. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyWorkersResponse) -> dict:
    out: dict = {}
    if "notify_workers_failure_statuses" in value:
        import aws_sdk_mturk.types.notify_workers_failure_status_list

        out["NotifyWorkersFailureStatuses"] = (
            aws_sdk_mturk.types.notify_workers_failure_status_list.serialize_aws_json_1_1(
                value["notify_workers_failure_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyWorkersResponse:
    out: NotifyWorkersResponse = {}  # type: ignore[typeddict-item]
    if "NotifyWorkersFailureStatuses" in data:
        import aws_sdk_mturk.types.notify_workers_failure_status_list

        out["notify_workers_failure_statuses"] = (
            aws_sdk_mturk.types.notify_workers_failure_status_list.deserialize_aws_json_1_1(
                data["NotifyWorkersFailureStatuses"]
            )
        )
    return out
