"""Generated from Smithy shape ``com.amazonaws.batch#CreateQuotaShareRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_capacity_limits
    import aws_sdk_batch.types.quota_share_preemption_configuration
    import aws_sdk_batch.types.quota_share_resource_sharing_configuration
    import aws_sdk_batch.types.quota_share_state
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class CreateQuotaShareRequest(TypedDict):
    quota_share_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the quota share. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    job_queue: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Batch job queue associated with the quota share. This can be the job queue name or ARN. A job queue must be in the <code>VALID</code> state before you can associate it with a quota share.</p>"""
    capacity_limits: NotRequired[
        "aws_sdk_batch.types.quota_share_capacity_limits.QuotaShareCapacityLimits"
    ]
    """<p>A list that specifies the quantity and type of compute capacity allocated to the quota share. </p>"""
    resource_sharing_configuration: NotRequired[
        "aws_sdk_batch.types.quota_share_resource_sharing_configuration.QuotaShareResourceSharingConfiguration"
    ]
    """<p>Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.</p>"""
    preemption_configuration: NotRequired[
        "aws_sdk_batch.types.quota_share_preemption_configuration.QuotaSharePreemptionConfiguration"
    ]
    """<p>Specifies the preemption behavior for jobs in a quota share.</p>"""
    state: NotRequired["aws_sdk_batch.types.quota_share_state.QuotaShareState"]
    """<p>The state of the quota share. If the quota share is <code>ENABLED</code>, it is able to accept jobs. If the quota share is <code>DISABLED</code>, new jobs won't be accepted but jobs already submitted can finish. The default state is <code>ENABLED</code>.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that you apply to the quota share to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html\">Tagging your Batch resources</a> in <i>Batch User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuotaShareRequest) -> dict:
    out: dict = {}
    if "quota_share_name" in value:
        out["quotaShareName"] = value["quota_share_name"]
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
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
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateQuotaShareRequest:
    out: CreateQuotaShareRequest = {}  # type: ignore[typeddict-item]
    if "quotaShareName" in data:
        out["quota_share_name"] = data["quotaShareName"]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
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
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    return out
