"""Generated from Smithy shape ``com.amazonaws.iot#JobProcessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.canceled_things
    import capo_iot.types.failed_things
    import capo_iot.types.in_progress_things
    import capo_iot.types.processing_target_name_list
    import capo_iot.types.queued_things
    import capo_iot.types.rejected_things
    import capo_iot.types.removed_things
    import capo_iot.types.succeeded_things
    import capo_iot.types.timed_out_things


class JobProcessDetails(TypedDict, closed=True):
    processing_targets: NotRequired[
        "capo_iot.types.processing_target_name_list.ProcessingTargetNameList"
    ]
    """<p>The target devices to which the job execution is being rolled out. This value will be null after the job execution has finished rolling out to all the target devices.</p>"""
    number_of_canceled_things: NotRequired[
        "capo_iot.types.canceled_things.CanceledThings"
    ]
    """<p>The number of things that cancelled the job.</p>"""
    number_of_succeeded_things: NotRequired[
        "capo_iot.types.succeeded_things.SucceededThings"
    ]
    """<p>The number of things which successfully completed the job.</p>"""
    number_of_failed_things: NotRequired["capo_iot.types.failed_things.FailedThings"]
    """<p>The number of things that failed executing the job.</p>"""
    number_of_rejected_things: NotRequired[
        "capo_iot.types.rejected_things.RejectedThings"
    ]
    """<p>The number of things that rejected the job.</p>"""
    number_of_queued_things: NotRequired["capo_iot.types.queued_things.QueuedThings"]
    """<p>The number of things that are awaiting execution of the job.</p>"""
    number_of_in_progress_things: NotRequired[
        "capo_iot.types.in_progress_things.InProgressThings"
    ]
    """<p>The number of things currently executing the job.</p>"""
    number_of_removed_things: NotRequired["capo_iot.types.removed_things.RemovedThings"]
    """<p>The number of things that are no longer scheduled to execute the job because they have been deleted or have been removed from the group that was a target of the job.</p>"""
    number_of_timed_out_things: NotRequired[
        "capo_iot.types.timed_out_things.TimedOutThings"
    ]
    """<p>The number of things whose job execution status is <code>TIMED_OUT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobProcessDetails) -> dict:
    out: dict = {}
    if "processing_targets" in value:
        import capo_iot.types.processing_target_name_list

        out["processingTargets"] = (
            capo_iot.types.processing_target_name_list.serialize_json(
                value["processing_targets"]
            )
        )
    if "number_of_canceled_things" in value:
        out["numberOfCanceledThings"] = value["number_of_canceled_things"]
    if "number_of_succeeded_things" in value:
        out["numberOfSucceededThings"] = value["number_of_succeeded_things"]
    if "number_of_failed_things" in value:
        out["numberOfFailedThings"] = value["number_of_failed_things"]
    if "number_of_rejected_things" in value:
        out["numberOfRejectedThings"] = value["number_of_rejected_things"]
    if "number_of_queued_things" in value:
        out["numberOfQueuedThings"] = value["number_of_queued_things"]
    if "number_of_in_progress_things" in value:
        out["numberOfInProgressThings"] = value["number_of_in_progress_things"]
    if "number_of_removed_things" in value:
        out["numberOfRemovedThings"] = value["number_of_removed_things"]
    if "number_of_timed_out_things" in value:
        out["numberOfTimedOutThings"] = value["number_of_timed_out_things"]
    return out


def deserialize_json(data: dict) -> JobProcessDetails:
    out: JobProcessDetails = {}  # type: ignore[typeddict-item]
    if "processingTargets" in data:
        import capo_iot.types.processing_target_name_list

        out["processing_targets"] = (
            capo_iot.types.processing_target_name_list.deserialize_json(
                data["processingTargets"]
            )
        )
    if "numberOfCanceledThings" in data:
        out["number_of_canceled_things"] = data["numberOfCanceledThings"]
    if "numberOfSucceededThings" in data:
        out["number_of_succeeded_things"] = data["numberOfSucceededThings"]
    if "numberOfFailedThings" in data:
        out["number_of_failed_things"] = data["numberOfFailedThings"]
    if "numberOfRejectedThings" in data:
        out["number_of_rejected_things"] = data["numberOfRejectedThings"]
    if "numberOfQueuedThings" in data:
        out["number_of_queued_things"] = data["numberOfQueuedThings"]
    if "numberOfInProgressThings" in data:
        out["number_of_in_progress_things"] = data["numberOfInProgressThings"]
    if "numberOfRemovedThings" in data:
        out["number_of_removed_things"] = data["numberOfRemovedThings"]
    if "numberOfTimedOutThings" in data:
        out["number_of_timed_out_things"] = data["numberOfTimedOutThings"]
    return out
