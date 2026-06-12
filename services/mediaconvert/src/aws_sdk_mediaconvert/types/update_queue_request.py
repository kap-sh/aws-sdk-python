"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UpdateQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.__integer_min0
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.queue_status
    import aws_sdk_mediaconvert.types.reservation_plan_settings


class UpdateQueueRequest(TypedDict):
    concurrent_jobs: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, update your reservation plan instead in order to increase your yearly commitment."""
    description: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The new description for the queue, if you are changing it."""
    maximum_concurrent_feeds: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0.__integerMin0"
    ]
    """Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently."""
    name: "aws_sdk_mediaconvert.types.__string.__string"
    """The name of the queue that you are modifying."""
    reservation_plan_settings: NotRequired[
        "aws_sdk_mediaconvert.types.reservation_plan_settings.ReservationPlanSettings"
    ]
    """The new details of your pricing plan for your reserved queue. When you set up a new pricing plan to replace an expired one, you enter into another 12-month commitment. When you add capacity to your queue by increasing the number of RTS, you extend the term of your commitment to 12 months from when you add capacity. After you make these commitments, you can't cancel them."""
    status: NotRequired["aws_sdk_mediaconvert.types.queue_status.QueueStatus"]
    """Pause or activate a queue by changing its status between ACTIVE and PAUSED. If you pause a queue, jobs in that queue won't begin. Jobs that are running when you pause the queue continue to run until they finish or result in an error."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueRequest) -> dict:
    out: dict = {}
    if "concurrent_jobs" in value:
        out["concurrentJobs"] = value["concurrent_jobs"]
    if "description" in value:
        out["description"] = value["description"]
    if "maximum_concurrent_feeds" in value:
        out["maximumConcurrentFeeds"] = value["maximum_concurrent_feeds"]
    if "reservation_plan_settings" in value:
        import aws_sdk_mediaconvert.types.reservation_plan_settings

        out["reservationPlanSettings"] = (
            aws_sdk_mediaconvert.types.reservation_plan_settings.serialize_json(
                value["reservation_plan_settings"]
            )
        )
    if "status" in value:
        import aws_sdk_mediaconvert.types.queue_status

        out["status"] = aws_sdk_mediaconvert.types.queue_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateQueueRequest:
    out: UpdateQueueRequest = {}  # type: ignore[typeddict-item]
    if "concurrentJobs" in data:
        out["concurrent_jobs"] = data["concurrentJobs"]
    if "description" in data:
        out["description"] = data["description"]
    if "maximumConcurrentFeeds" in data:
        out["maximum_concurrent_feeds"] = data["maximumConcurrentFeeds"]
    if "reservationPlanSettings" in data:
        import aws_sdk_mediaconvert.types.reservation_plan_settings

        out["reservation_plan_settings"] = (
            aws_sdk_mediaconvert.types.reservation_plan_settings.deserialize_json(
                data["reservationPlanSettings"]
            )
        )
    if "status" in data:
        import aws_sdk_mediaconvert.types.queue_status

        out["status"] = aws_sdk_mediaconvert.types.queue_status.deserialize_json(
            data["status"]
        )
    return out
