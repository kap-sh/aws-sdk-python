"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ResourceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.readiness
    import aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp


class ResourceResult(TypedDict):
    component_id: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The component id of the resource.</p>"""
    last_checked_timestamp: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp.ReadinessCheckTimestamp"
    ]
    """<p>The time (UTC) that the resource was last checked for readiness, in ISO-8601 format.</p>"""
    readiness: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.readiness.Readiness"
    ]
    """<p>The readiness of a resource.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceResult) -> dict:
    out: dict = {}
    if "component_id" in value:
        out["componentId"] = value["component_id"]
    if "last_checked_timestamp" in value:
        import aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp

        out["lastCheckedTimestamp"] = (
            aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp.serialize_json(
                value["last_checked_timestamp"]
            )
        )
    if "readiness" in value:
        import aws_sdk_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            aws_sdk_route53_recovery_readiness.types.readiness.serialize_json(
                value["readiness"]
            )
        )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ResourceResult:
    out: ResourceResult = {}  # type: ignore[typeddict-item]
    if "componentId" in data:
        out["component_id"] = data["componentId"]
    if "lastCheckedTimestamp" in data:
        import aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp

        out["last_checked_timestamp"] = (
            aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp.deserialize_json(
                data["lastCheckedTimestamp"]
            )
        )
    if "readiness" in data:
        import aws_sdk_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            aws_sdk_route53_recovery_readiness.types.readiness.deserialize_json(
                data["readiness"]
            )
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    return out
