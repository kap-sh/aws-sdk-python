"""Generated from Smithy shape ``com.amazonaws.batch#DescribeQuotaShareResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_capacity_limits
    import aws_sdk_batch.types.quota_share_preemption_configuration
    import aws_sdk_batch.types.quota_share_resource_sharing_configuration
    import aws_sdk_batch.types.quota_share_state
    import aws_sdk_batch.types.quota_share_status
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class DescribeQuotaShareResponse(TypedDict):
    quota_share_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the quota share.</p>"""
    quota_share_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the quota share.</p>"""
    job_queue_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The ARN of the job queue associated with the quota share.</p>"""
    capacity_limits: NotRequired[
        "aws_sdk_batch.types.quota_share_capacity_limits.QuotaShareCapacityLimits"
    ]
    """<p>A list that specifies the quantity and type of compute capacity allocated to the quota share.</p>"""
    resource_sharing_configuration: NotRequired[
        "aws_sdk_batch.types.quota_share_resource_sharing_configuration.QuotaShareResourceSharingConfiguration"
    ]
    """<p>Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.</p>"""
    preemption_configuration: NotRequired[
        "aws_sdk_batch.types.quota_share_preemption_configuration.QuotaSharePreemptionConfiguration"
    ]
    """<p>Specifies the preemption behavior for jobs in a quota share.</p>"""
    state: NotRequired["aws_sdk_batch.types.quota_share_state.QuotaShareState"]
    """<p>The state of the quota share.</p>"""
    status: NotRequired["aws_sdk_batch.types.quota_share_status.QuotaShareStatus"]
    """<p>The current status of the quota share.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags applied to the quota share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQuotaShareResponse) -> dict:
    out: dict = {}
    if "quota_share_name" in value:
        out["quotaShareName"] = value["quota_share_name"]
    if "quota_share_arn" in value:
        out["quotaShareArn"] = value["quota_share_arn"]
    if "job_queue_arn" in value:
        out["jobQueueArn"] = value["job_queue_arn"]
    if "capacity_limits" in value:
        import aws_sdk_batch.types.quota_share_capacity_limits

        out["capacityLimits"] = (
            aws_sdk_batch.types.quota_share_capacity_limits.serialize_json(
                value["capacity_limits"]
            )
        )
    if "resource_sharing_configuration" in value:
        import aws_sdk_batch.types.quota_share_resource_sharing_configuration

        out["resourceSharingConfiguration"] = (
            aws_sdk_batch.types.quota_share_resource_sharing_configuration.serialize_json(
                value["resource_sharing_configuration"]
            )
        )
    if "preemption_configuration" in value:
        import aws_sdk_batch.types.quota_share_preemption_configuration

        out["preemptionConfiguration"] = (
            aws_sdk_batch.types.quota_share_preemption_configuration.serialize_json(
                value["preemption_configuration"]
            )
        )
    if "state" in value:
        import aws_sdk_batch.types.quota_share_state

        out["state"] = aws_sdk_batch.types.quota_share_state.serialize_json(
            value["state"]
        )
    if "status" in value:
        import aws_sdk_batch.types.quota_share_status

        out["status"] = aws_sdk_batch.types.quota_share_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeQuotaShareResponse:
    out: DescribeQuotaShareResponse = {}  # type: ignore[typeddict-item]
    if "quotaShareName" in data:
        out["quota_share_name"] = data["quotaShareName"]
    if "quotaShareArn" in data:
        out["quota_share_arn"] = data["quotaShareArn"]
    if "jobQueueArn" in data:
        out["job_queue_arn"] = data["jobQueueArn"]
    if "capacityLimits" in data:
        import aws_sdk_batch.types.quota_share_capacity_limits

        out["capacity_limits"] = (
            aws_sdk_batch.types.quota_share_capacity_limits.deserialize_json(
                data["capacityLimits"]
            )
        )
    if "resourceSharingConfiguration" in data:
        import aws_sdk_batch.types.quota_share_resource_sharing_configuration

        out["resource_sharing_configuration"] = (
            aws_sdk_batch.types.quota_share_resource_sharing_configuration.deserialize_json(
                data["resourceSharingConfiguration"]
            )
        )
    if "preemptionConfiguration" in data:
        import aws_sdk_batch.types.quota_share_preemption_configuration

        out["preemption_configuration"] = (
            aws_sdk_batch.types.quota_share_preemption_configuration.deserialize_json(
                data["preemptionConfiguration"]
            )
        )
    if "state" in data:
        import aws_sdk_batch.types.quota_share_state

        out["state"] = aws_sdk_batch.types.quota_share_state.deserialize_json(
            data["state"]
        )
    if "status" in data:
        import aws_sdk_batch.types.quota_share_status

        out["status"] = aws_sdk_batch.types.quota_share_status.deserialize_json(
            data["status"]
        )
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    return out
