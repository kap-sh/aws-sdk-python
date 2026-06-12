"""Generated from Smithy shape ``com.amazonaws.iot#SecurityProfileTarget``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.security_profile_target_arn


class SecurityProfileTarget(TypedDict):
    arn: "aws_sdk_iot.types.security_profile_target_arn.SecurityProfileTargetArn"
    """<p>The ARN of the security profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileTarget) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> SecurityProfileTarget:
    out: SecurityProfileTarget = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SecurityProfileTarget.arn required")
    return out
