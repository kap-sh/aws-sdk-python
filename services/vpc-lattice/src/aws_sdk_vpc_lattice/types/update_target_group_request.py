"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateTargetGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.health_check_config
    import aws_sdk_vpc_lattice.types.target_group_identifier


class UpdateTargetGroupRequest(TypedDict):
    target_group_identifier: (
        "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier"
    )
    """<p>The ID or ARN of the target group.</p>"""
    health_check: "aws_sdk_vpc_lattice.types.health_check_config.HealthCheckConfig"
    """<p>The health check configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTargetGroupRequest) -> dict:
    out: dict = {}
    import aws_sdk_vpc_lattice.types.health_check_config

    out["healthCheck"] = aws_sdk_vpc_lattice.types.health_check_config.serialize_json(
        value["health_check"]
    )
    return out


def deserialize_json(data: dict) -> UpdateTargetGroupRequest:
    out: UpdateTargetGroupRequest = {}  # type: ignore[typeddict-item]
    if "healthCheck" in data:
        import aws_sdk_vpc_lattice.types.health_check_config

        out["health_check"] = (
            aws_sdk_vpc_lattice.types.health_check_config.deserialize_json(
                data["healthCheck"]
            )
        )
    else:
        raise DeserializationError("UpdateTargetGroupRequest.health_check required")
    return out
