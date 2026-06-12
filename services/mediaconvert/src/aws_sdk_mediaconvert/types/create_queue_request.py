"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CreateQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.__integer_min0
    import aws_sdk_mediaconvert.types.__map_of__string
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.pricing_plan
    import aws_sdk_mediaconvert.types.queue_status
    import aws_sdk_mediaconvert.types.reservation_plan_settings


class CreateQueueRequest(TypedDict):
    concurrent_jobs: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, specify the number of jobs you can process concurrently in your reservation plan instead."""
    description: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. A description of the queue that you are creating."""
    maximum_concurrent_feeds: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0.__integerMin0"
    ]
    """Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently."""
    name: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The name of the queue that you are creating."""
    pricing_plan: NotRequired["aws_sdk_mediaconvert.types.pricing_plan.PricingPlan"]
    """Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment. When you use the API to create a queue, the default is on-demand."""
    reservation_plan_settings: NotRequired[
        "aws_sdk_mediaconvert.types.reservation_plan_settings.ReservationPlanSettings"
    ]
    """Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues."""
    status: NotRequired["aws_sdk_mediaconvert.types.queue_status.QueueStatus"]
    """Initial state of the queue. If you create a paused queue, then jobs in that queue won't begin."""
    tags: NotRequired["aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"]
    """The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueRequest) -> dict:
    out: dict = {}
    if "concurrent_jobs" in value:
        out["concurrentJobs"] = value["concurrent_jobs"]
    if "description" in value:
        out["description"] = value["description"]
    if "maximum_concurrent_feeds" in value:
        out["maximumConcurrentFeeds"] = value["maximum_concurrent_feeds"]
    if "name" in value:
        out["name"] = value["name"]
    if "pricing_plan" in value:
        import aws_sdk_mediaconvert.types.pricing_plan

        out["pricingPlan"] = aws_sdk_mediaconvert.types.pricing_plan.serialize_json(
            value["pricing_plan"]
        )
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
    if "tags" in value:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["tags"] = aws_sdk_mediaconvert.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateQueueRequest:
    out: CreateQueueRequest = {}  # type: ignore[typeddict-item]
    if "concurrentJobs" in data:
        out["concurrent_jobs"] = data["concurrentJobs"]
    if "description" in data:
        out["description"] = data["description"]
    if "maximumConcurrentFeeds" in data:
        out["maximum_concurrent_feeds"] = data["maximumConcurrentFeeds"]
    if "name" in data:
        out["name"] = data["name"]
    if "pricingPlan" in data:
        import aws_sdk_mediaconvert.types.pricing_plan

        out["pricing_plan"] = aws_sdk_mediaconvert.types.pricing_plan.deserialize_json(
            data["pricingPlan"]
        )
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
    if "tags" in data:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["tags"] = aws_sdk_mediaconvert.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
