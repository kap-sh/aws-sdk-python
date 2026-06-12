"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Queue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.__integer_min0
    import aws_sdk_mediaconvert.types.__list_of_service_override
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.__timestamp_unix
    import aws_sdk_mediaconvert.types.pricing_plan
    import aws_sdk_mediaconvert.types.queue_status
    import aws_sdk_mediaconvert.types.reservation_plan
    import aws_sdk_mediaconvert.types.type


class Queue(TypedDict):
    arn: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """An identifier for this resource that is unique within all of AWS."""
    concurrent_jobs: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The maximum number of jobs your queue can process concurrently."""
    created_at: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The timestamp in epoch seconds for when you created the queue."""
    description: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """An optional description that you create for each queue."""
    last_updated: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The timestamp in epoch seconds for when you most recently updated the queue."""
    maximum_concurrent_feeds: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0.__integerMin0"
    ]
    """Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently."""
    name: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """A name that you create for each queue. Each name must be unique within your account."""
    pricing_plan: NotRequired["aws_sdk_mediaconvert.types.pricing_plan.PricingPlan"]
    """Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment."""
    progressing_jobs_count: NotRequired[
        "aws_sdk_mediaconvert.types.__integer.__integer"
    ]
    """The estimated number of jobs with a PROGRESSING status."""
    reservation_plan: NotRequired[
        "aws_sdk_mediaconvert.types.reservation_plan.ReservationPlan"
    ]
    """Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues."""
    service_overrides: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_service_override.__listOfServiceOverride"
    ]
    """A list of any service overrides applied by MediaConvert to the settings that you have configured. If you see any overrides, we recommend that you contact AWS Support."""
    status: NotRequired["aws_sdk_mediaconvert.types.queue_status.QueueStatus"]
    """Queues can be ACTIVE or PAUSED. If you pause a queue, the service won't begin processing jobs in that queue. Jobs that are running when you pause the queue continue to run until they finish or result in an error."""
    submitted_jobs_count: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The estimated number of jobs with a SUBMITTED status."""
    type: NotRequired["aws_sdk_mediaconvert.types.type.Type"]
    """Specifies whether this on-demand queue is system or custom. System queues are built in. You can't modify or delete system queues. You can create and modify custom queues."""


# --- restJson1 ser/de ---
def serialize_json(value: Queue) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "concurrent_jobs" in value:
        out["concurrentJobs"] = value["concurrent_jobs"]
    if "created_at" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["createdAt"] = aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "last_updated" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["lastUpdated"] = aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
            value["last_updated"]
        )
    if "maximum_concurrent_feeds" in value:
        out["maximumConcurrentFeeds"] = value["maximum_concurrent_feeds"]
    if "name" in value:
        out["name"] = value["name"]
    if "pricing_plan" in value:
        import aws_sdk_mediaconvert.types.pricing_plan

        out["pricingPlan"] = aws_sdk_mediaconvert.types.pricing_plan.serialize_json(
            value["pricing_plan"]
        )
    if "progressing_jobs_count" in value:
        out["progressingJobsCount"] = value["progressing_jobs_count"]
    if "reservation_plan" in value:
        import aws_sdk_mediaconvert.types.reservation_plan

        out["reservationPlan"] = (
            aws_sdk_mediaconvert.types.reservation_plan.serialize_json(
                value["reservation_plan"]
            )
        )
    if "service_overrides" in value:
        import aws_sdk_mediaconvert.types.__list_of_service_override

        out["serviceOverrides"] = (
            aws_sdk_mediaconvert.types.__list_of_service_override.serialize_json(
                value["service_overrides"]
            )
        )
    if "status" in value:
        import aws_sdk_mediaconvert.types.queue_status

        out["status"] = aws_sdk_mediaconvert.types.queue_status.serialize_json(
            value["status"]
        )
    if "submitted_jobs_count" in value:
        out["submittedJobsCount"] = value["submitted_jobs_count"]
    if "type" in value:
        import aws_sdk_mediaconvert.types.type

        out["type"] = aws_sdk_mediaconvert.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Queue:
    out: Queue = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "concurrentJobs" in data:
        out["concurrent_jobs"] = data["concurrentJobs"]
    if "createdAt" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["created_at"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["createdAt"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "lastUpdated" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["last_updated"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["lastUpdated"]
            )
        )
    if "maximumConcurrentFeeds" in data:
        out["maximum_concurrent_feeds"] = data["maximumConcurrentFeeds"]
    if "name" in data:
        out["name"] = data["name"]
    if "pricingPlan" in data:
        import aws_sdk_mediaconvert.types.pricing_plan

        out["pricing_plan"] = aws_sdk_mediaconvert.types.pricing_plan.deserialize_json(
            data["pricingPlan"]
        )
    if "progressingJobsCount" in data:
        out["progressing_jobs_count"] = data["progressingJobsCount"]
    if "reservationPlan" in data:
        import aws_sdk_mediaconvert.types.reservation_plan

        out["reservation_plan"] = (
            aws_sdk_mediaconvert.types.reservation_plan.deserialize_json(
                data["reservationPlan"]
            )
        )
    if "serviceOverrides" in data:
        import aws_sdk_mediaconvert.types.__list_of_service_override

        out["service_overrides"] = (
            aws_sdk_mediaconvert.types.__list_of_service_override.deserialize_json(
                data["serviceOverrides"]
            )
        )
    if "status" in data:
        import aws_sdk_mediaconvert.types.queue_status

        out["status"] = aws_sdk_mediaconvert.types.queue_status.deserialize_json(
            data["status"]
        )
    if "submittedJobsCount" in data:
        out["submitted_jobs_count"] = data["submittedJobsCount"]
    if "type" in data:
        import aws_sdk_mediaconvert.types.type

        out["type"] = aws_sdk_mediaconvert.types.type.deserialize_json(data["type"])
    return out
