"""Generated from Smithy shape ``com.amazonaws.deadline#Statistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.instance_type
    import aws_sdk_deadline.types.integer
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.job_name
    import aws_sdk_deadline.types.license_product
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.stats
    import aws_sdk_deadline.types.timestamp
    import aws_sdk_deadline.types.usage_type
    import aws_sdk_deadline.types.user_id


class Statistics(TypedDict):
    queue_id: NotRequired["aws_sdk_deadline.types.queue_id.QueueId"]
    """<p>The queue ID.</p>"""
    fleet_id: NotRequired["aws_sdk_deadline.types.fleet_id.FleetId"]
    """<p>The fleet ID.</p>"""
    job_id: NotRequired["aws_sdk_deadline.types.job_id.JobId"]
    """<p>The job ID.</p>"""
    job_name: NotRequired["aws_sdk_deadline.types.job_name.JobName"]
    """<p>The job name.</p>"""
    user_id: NotRequired["aws_sdk_deadline.types.user_id.UserId"]
    """<p>The user ID.</p>"""
    usage_type: NotRequired["aws_sdk_deadline.types.usage_type.UsageType"]
    """<p>The type of usage for the statistics.</p>"""
    license_product: NotRequired[
        "aws_sdk_deadline.types.license_product.LicenseProduct"
    ]
    """<p>The licensed product.</p>"""
    instance_type: NotRequired["aws_sdk_deadline.types.instance_type.InstanceType"]
    """<p>The type of instance.</p>"""
    count: "aws_sdk_deadline.types.integer.Integer"
    """<p>The number of instances in a list of statistics.</p>"""
    cost_in_usd: "aws_sdk_deadline.types.stats.Stats"
    """<p>How the statistics should appear in USD. Options include: minimum, maximum, average or sum.</p>"""
    runtime_in_seconds: "aws_sdk_deadline.types.stats.Stats"
    """<p>The total aggregated runtime.</p>"""
    aggregation_start_time: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The start time for the aggregation.</p>"""
    aggregation_end_time: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The end time for the aggregation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Statistics) -> dict:
    out: dict = {}
    if "queue_id" in value:
        out["queueId"] = value["queue_id"]
    if "fleet_id" in value:
        out["fleetId"] = value["fleet_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "usage_type" in value:
        import aws_sdk_deadline.types.usage_type

        out["usageType"] = aws_sdk_deadline.types.usage_type.serialize_json(
            value["usage_type"]
        )
    if "license_product" in value:
        out["licenseProduct"] = value["license_product"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    out["count"] = value["count"]
    import aws_sdk_deadline.types.stats

    out["costInUsd"] = aws_sdk_deadline.types.stats.serialize_json(value["cost_in_usd"])
    import aws_sdk_deadline.types.stats

    out["runtimeInSeconds"] = aws_sdk_deadline.types.stats.serialize_json(
        value["runtime_in_seconds"]
    )
    if "aggregation_start_time" in value:
        import aws_sdk_deadline.types.timestamp

        out["aggregationStartTime"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["aggregation_start_time"]
        )
    if "aggregation_end_time" in value:
        import aws_sdk_deadline.types.timestamp

        out["aggregationEndTime"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["aggregation_end_time"]
        )
    return out


def deserialize_json(data: dict) -> Statistics:
    out: Statistics = {}  # type: ignore[typeddict-item]
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "usageType" in data:
        import aws_sdk_deadline.types.usage_type

        out["usage_type"] = aws_sdk_deadline.types.usage_type.deserialize_json(
            data["usageType"]
        )
    if "licenseProduct" in data:
        out["license_product"] = data["licenseProduct"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "count" in data:
        out["count"] = data["count"]
    else:
        raise DeserializationError("Statistics.count required")
    if "costInUsd" in data:
        import aws_sdk_deadline.types.stats

        out["cost_in_usd"] = aws_sdk_deadline.types.stats.deserialize_json(
            data["costInUsd"]
        )
    else:
        raise DeserializationError("Statistics.cost_in_usd required")
    if "runtimeInSeconds" in data:
        import aws_sdk_deadline.types.stats

        out["runtime_in_seconds"] = aws_sdk_deadline.types.stats.deserialize_json(
            data["runtimeInSeconds"]
        )
    else:
        raise DeserializationError("Statistics.runtime_in_seconds required")
    if "aggregationStartTime" in data:
        import aws_sdk_deadline.types.timestamp

        out["aggregation_start_time"] = (
            aws_sdk_deadline.types.timestamp.deserialize_json(
                data["aggregationStartTime"]
            )
        )
    if "aggregationEndTime" in data:
        import aws_sdk_deadline.types.timestamp

        out["aggregation_end_time"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["aggregationEndTime"]
        )
    return out
