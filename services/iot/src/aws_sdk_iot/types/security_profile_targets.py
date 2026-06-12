"""Generated from Smithy shape ``com.amazonaws.iot#SecurityProfileTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.security_profile_target

SecurityProfileTargets: TypeAlias = list[
    "aws_sdk_iot.types.security_profile_target.SecurityProfileTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileTargets) -> list:
    import aws_sdk_iot.types.security_profile_target

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.security_profile_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityProfileTargets:
    import aws_sdk_iot.types.security_profile_target

    out: SecurityProfileTargets = []
    for item in data:
        out.append(aws_sdk_iot.types.security_profile_target.deserialize_json(item))
    return out
