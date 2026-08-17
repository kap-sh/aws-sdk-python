"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedMetricAlarm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.managed_resource_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class ManagedMetricAlarm(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch metric alarm.</p>"""
    status: "capo_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the CloudWatch metric alarm.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>Information about why the CloudWatch metric alarm is in the current status.</p>"""
    updated_at: "capo_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the CloudWatch metric alarm was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedMetricAlarm) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    import capo_ecs.types.managed_resource_status

    out["status"] = capo_ecs.types.managed_resource_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_ecs.types.timestamp

    out["updatedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedMetricAlarm:
    out: ManagedMetricAlarm = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        import capo_ecs.types.managed_resource_status

        out["status"] = capo_ecs.types.managed_resource_status.deserialize_aws_json_1_1(
            data["status"]
        )
    else:
        raise DeserializationError("ManagedMetricAlarm.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("updatedAt") is not None:
        import capo_ecs.types.timestamp

        out["updated_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ManagedMetricAlarm.updated_at required")
    return out
