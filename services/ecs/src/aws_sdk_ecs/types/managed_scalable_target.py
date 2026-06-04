"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedScalableTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedScalableTarget(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the scalable target.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the scalable target.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the scalable target is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the target was most recently updated.</p>"""
    min_capacity: "aws_sdk_ecs.types.integer.Integer"
    """<p>The minimum value to scale to in response to a scale-in activity.</p>"""
    max_capacity: "aws_sdk_ecs.types.integer.Integer"
    """<p>The maximum value to scale to in response to a scale-out activity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedScalableTarget) -> dict:
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
    out["minCapacity"] = value.get("min_capacity", 0)
    out["maxCapacity"] = value.get("max_capacity", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedScalableTarget:
    out: ManagedScalableTarget = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("ManagedScalableTarget.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "updatedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["updated_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ManagedScalableTarget.updated_at required")
    if "minCapacity" in data:
        out["min_capacity"] = data["minCapacity"]
    else:
        out["min_capacity"] = 0
    if "maxCapacity" in data:
        out["max_capacity"] = data["maxCapacity"]
    else:
        out["max_capacity"] = 0
    return out
