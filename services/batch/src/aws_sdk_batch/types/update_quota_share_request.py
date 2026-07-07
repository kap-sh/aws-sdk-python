"""Generated from Smithy shape ``com.amazonaws.batch#UpdateQuotaShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_capacity_limits
    import aws_sdk_batch.types.quota_share_preemption_configuration
    import aws_sdk_batch.types.quota_share_resource_sharing_configuration
    import aws_sdk_batch.types.quota_share_state
    import aws_sdk_batch.types.string


class UpdateQuotaShareRequest(TypedDict, closed=True):
    quota_share_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the quota share to update.</p>"""
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
    """<p>The state of the quota share. If the quota share is <code>ENABLED</code>, it is able to accept jobs. If the quota share is <code>DISABLED</code>, new jobs won't be accepted but jobs already submitted can finish.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuotaShareRequest) -> dict:
    out: dict = {}
    if "quota_share_arn" in value:
        out["quotaShareArn"] = value["quota_share_arn"]
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
    return out


def deserialize_json(data: dict) -> UpdateQuotaShareRequest:
    out: UpdateQuotaShareRequest = {}  # type: ignore[typeddict-item]
    if "quotaShareArn" in data:
        out["quota_share_arn"] = data["quotaShareArn"]
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
    return out
