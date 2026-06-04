"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedTargetGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedTargetGroup(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the target group.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the target group is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the target group was last updated.</p>"""
    health_check_path: "aws_sdk_ecs.types.string.String"
    """<p>The destination for health checks on the targets.</p>"""
    health_check_port: "aws_sdk_ecs.types.integer.Integer"
    """<p>The port the load balancer uses when performing health checks on targets.</p>"""
    port: "aws_sdk_ecs.types.integer.Integer"
    """<p>The port on which the targets receive traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedTargetGroup) -> dict:
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
    out["healthCheckPath"] = value["health_check_path"]
    out["healthCheckPort"] = value.get("health_check_port", 0)
    out["port"] = value.get("port", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedTargetGroup:
    out: ManagedTargetGroup = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("ManagedTargetGroup.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "updatedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["updated_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ManagedTargetGroup.updated_at required")
    if "healthCheckPath" in data:
        out["health_check_path"] = data["healthCheckPath"]
    else:
        raise DeserializationError("ManagedTargetGroup.health_check_path required")
    if "healthCheckPort" in data:
        out["health_check_port"] = data["healthCheckPort"]
    else:
        out["health_check_port"] = 0
    if "port" in data:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    return out
