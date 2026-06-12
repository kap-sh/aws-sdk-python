"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#TaskProcessingDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.target


class TaskProcessingDetails(TypedDict):
    number_of_canceled_things: NotRequired["int"]
    """<p>The number of canceled things in an over-the-air (OTA) task.</p>"""
    number_of_failed_things: NotRequired["int"]
    """<p>The number of failed things in an over-the-air (OTA) task.</p>"""
    number_of_in_progress_things: NotRequired["int"]
    """<p>The number of in progress things in an over-the-air (OTA) task.</p>"""
    number_of_queued_things: NotRequired["int"]
    """<p>The number of queued things in an over-the-air (OTA) task.</p>"""
    number_of_rejected_things: NotRequired["int"]
    """<p>The number of rejected things in an over-the-air (OTA) task.</p>"""
    number_of_removed_things: NotRequired["int"]
    """<p>The number of removed things in an over-the-air (OTA) task.</p>"""
    number_of_succeeded_things: NotRequired["int"]
    """<p>The number of succeeded things in an over-the-air (OTA) task.</p>"""
    number_of_timed_out_things: NotRequired["int"]
    """<p>The number of timed out things in an over-the-air (OTA) task.</p>"""
    processing_targets: NotRequired[
        "aws_sdk_iot_managed_integrations.types.target.Target"
    ]
    """<p>The targets of the over-the-air (OTA) task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskProcessingDetails) -> dict:
    out: dict = {}
    if "number_of_canceled_things" in value:
        out["NumberOfCanceledThings"] = value["number_of_canceled_things"]
    if "number_of_failed_things" in value:
        out["NumberOfFailedThings"] = value["number_of_failed_things"]
    if "number_of_in_progress_things" in value:
        out["NumberOfInProgressThings"] = value["number_of_in_progress_things"]
    if "number_of_queued_things" in value:
        out["numberOfQueuedThings"] = value["number_of_queued_things"]
    if "number_of_rejected_things" in value:
        out["numberOfRejectedThings"] = value["number_of_rejected_things"]
    if "number_of_removed_things" in value:
        out["numberOfRemovedThings"] = value["number_of_removed_things"]
    if "number_of_succeeded_things" in value:
        out["numberOfSucceededThings"] = value["number_of_succeeded_things"]
    if "number_of_timed_out_things" in value:
        out["numberOfTimedOutThings"] = value["number_of_timed_out_things"]
    if "processing_targets" in value:
        import aws_sdk_iot_managed_integrations.types.target

        out["processingTargets"] = (
            aws_sdk_iot_managed_integrations.types.target.serialize_json(
                value["processing_targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> TaskProcessingDetails:
    out: TaskProcessingDetails = {}  # type: ignore[typeddict-item]
    if "NumberOfCanceledThings" in data:
        out["number_of_canceled_things"] = data["NumberOfCanceledThings"]
    if "NumberOfFailedThings" in data:
        out["number_of_failed_things"] = data["NumberOfFailedThings"]
    if "NumberOfInProgressThings" in data:
        out["number_of_in_progress_things"] = data["NumberOfInProgressThings"]
    if "numberOfQueuedThings" in data:
        out["number_of_queued_things"] = data["numberOfQueuedThings"]
    if "numberOfRejectedThings" in data:
        out["number_of_rejected_things"] = data["numberOfRejectedThings"]
    if "numberOfRemovedThings" in data:
        out["number_of_removed_things"] = data["numberOfRemovedThings"]
    if "numberOfSucceededThings" in data:
        out["number_of_succeeded_things"] = data["numberOfSucceededThings"]
    if "numberOfTimedOutThings" in data:
        out["number_of_timed_out_things"] = data["numberOfTimedOutThings"]
    if "processingTargets" in data:
        import aws_sdk_iot_managed_integrations.types.target

        out["processing_targets"] = (
            aws_sdk_iot_managed_integrations.types.target.deserialize_json(
                data["processingTargets"]
            )
        )
    return out
