"""Generated from Smithy shape ``com.amazonaws.mturk#NotifyWorkersFailureStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.customer_id
    import aws_sdk_mturk.types.notify_workers_failure_code
    import aws_sdk_mturk.types.string


class NotifyWorkersFailureStatus(TypedDict, closed=True):
    notify_workers_failure_code: NotRequired[
        "aws_sdk_mturk.types.notify_workers_failure_code.NotifyWorkersFailureCode"
    ]
    """<p> Encoded value for the failure type. </p>"""
    notify_workers_failure_message: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> A message detailing the reason the Worker could not be notified. </p>"""
    worker_id: NotRequired["aws_sdk_mturk.types.customer_id.CustomerId"]
    """<p> The ID of the Worker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyWorkersFailureStatus) -> dict:
    out: dict = {}
    if "notify_workers_failure_code" in value:
        import aws_sdk_mturk.types.notify_workers_failure_code

        out["NotifyWorkersFailureCode"] = (
            aws_sdk_mturk.types.notify_workers_failure_code.serialize_aws_json_1_1(
                value["notify_workers_failure_code"]
            )
        )
    if "notify_workers_failure_message" in value:
        out["NotifyWorkersFailureMessage"] = value["notify_workers_failure_message"]
    if "worker_id" in value:
        out["WorkerId"] = value["worker_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyWorkersFailureStatus:
    out: NotifyWorkersFailureStatus = {}  # type: ignore[typeddict-item]
    if "NotifyWorkersFailureCode" in data:
        import aws_sdk_mturk.types.notify_workers_failure_code

        out["notify_workers_failure_code"] = (
            aws_sdk_mturk.types.notify_workers_failure_code.deserialize_aws_json_1_1(
                data["NotifyWorkersFailureCode"]
            )
        )
    if "NotifyWorkersFailureMessage" in data:
        out["notify_workers_failure_message"] = data["NotifyWorkersFailureMessage"]
    if "WorkerId" in data:
        out["worker_id"] = data["WorkerId"]
    return out
