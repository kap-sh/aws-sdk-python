"""Generated from Smithy shape ``com.amazonaws.guardduty#SecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.security_group

SecurityGroups: TypeAlias = list["aws_sdk_guardduty.types.security_group.SecurityGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroups) -> list:
    import aws_sdk_guardduty.types.security_group

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.security_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityGroups:
    import aws_sdk_guardduty.types.security_group

    out: SecurityGroups = []
    for item in data:
        out.append(aws_sdk_guardduty.types.security_group.deserialize_json(item))
    return out
