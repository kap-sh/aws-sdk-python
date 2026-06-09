"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.instance_health_check_state
    import aws_sdk_ecs.types.instance_health_check_type
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class InstanceHealthCheckResult(TypedDict):
    type: NotRequired[
        "aws_sdk_ecs.types.instance_health_check_type.InstanceHealthCheckType"
    ]
    """<p>The type of container instance health status that was verified.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.instance_health_check_state.InstanceHealthCheckState"
    ]
    """<p>The container instance health status.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for the container instance health status.</p>"""
    last_updated: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the container instance health status was last updated.</p>"""
    last_status_change: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the container instance health status last changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthCheckResult) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_ecs.types.instance_health_check_type

        out["type"] = (
            aws_sdk_ecs.types.instance_health_check_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "status" in value:
        import aws_sdk_ecs.types.instance_health_check_state

        out["status"] = (
            aws_sdk_ecs.types.instance_health_check_state.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "last_updated" in value:
        import aws_sdk_ecs.types.timestamp

        out["lastUpdated"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    if "last_status_change" in value:
        import aws_sdk_ecs.types.timestamp

        out["lastStatusChange"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["last_status_change"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceHealthCheckResult:
    out: InstanceHealthCheckResult = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_ecs.types.instance_health_check_type

        out["type"] = (
            aws_sdk_ecs.types.instance_health_check_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "status" in data:
        import aws_sdk_ecs.types.instance_health_check_state

        out["status"] = (
            aws_sdk_ecs.types.instance_health_check_state.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "lastUpdated" in data:
        import aws_sdk_ecs.types.timestamp

        out["last_updated"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["lastUpdated"]
        )
    if "lastStatusChange" in data:
        import aws_sdk_ecs.types.timestamp

        out["last_status_change"] = (
            aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
                data["lastStatusChange"]
            )
        )
    return out
