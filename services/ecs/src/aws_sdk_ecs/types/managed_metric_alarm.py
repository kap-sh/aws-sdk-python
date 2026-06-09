"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedMetricAlarm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedMetricAlarm(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch metric alarm.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the CloudWatch metric alarm.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the CloudWatch metric alarm is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the CloudWatch metric alarm was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedMetricAlarm) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    import aws_sdk_ecs.types.managed_resource_status

    out["status"] = aws_sdk_ecs.types.managed_resource_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import aws_sdk_ecs.types.timestamp

    out["updatedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedMetricAlarm:
    out: ManagedMetricAlarm = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import aws_sdk_ecs.types.managed_resource_status

        out["status"] = (
            aws_sdk_ecs.types.managed_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ManagedMetricAlarm.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "updatedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["updated_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ManagedMetricAlarm.updated_at required")
    return out
