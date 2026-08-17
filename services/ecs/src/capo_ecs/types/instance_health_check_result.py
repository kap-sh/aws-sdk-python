"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.instance_health_check_state
    import capo_ecs.types.instance_health_check_type
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class InstanceHealthCheckResult(TypedDict, closed=True):
    type: NotRequired[
        "capo_ecs.types.instance_health_check_type.InstanceHealthCheckType"
    ]
    """<p>The type of container instance health status that was verified.</p>"""
    status: NotRequired[
        "capo_ecs.types.instance_health_check_state.InstanceHealthCheckState"
    ]
    """<p>The container instance health status.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>The reason for the container instance health status.</p>"""
    last_updated: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the container instance health status was last updated.</p>"""
    last_status_change: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for when the container instance health status last changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthCheckResult) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_ecs.types.instance_health_check_type

        out["type"] = capo_ecs.types.instance_health_check_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import capo_ecs.types.instance_health_check_state

        out["status"] = (
            capo_ecs.types.instance_health_check_state.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "last_updated" in value:
        import capo_ecs.types.timestamp

        out["lastUpdated"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    if "last_status_change" in value:
        import capo_ecs.types.timestamp

        out["lastStatusChange"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["last_status_change"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceHealthCheckResult:
    out: InstanceHealthCheckResult = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_ecs.types.instance_health_check_type

        out["type"] = (
            capo_ecs.types.instance_health_check_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("status") is not None:
        import capo_ecs.types.instance_health_check_state

        out["status"] = (
            capo_ecs.types.instance_health_check_state.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("lastUpdated") is not None:
        import capo_ecs.types.timestamp

        out["last_updated"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["lastUpdated"]
        )
    if data.get("lastStatusChange") is not None:
        import capo_ecs.types.timestamp

        out["last_status_change"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["lastStatusChange"]
        )
    return out
