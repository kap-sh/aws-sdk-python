"""Generated from Smithy shape ``com.amazonaws.guardduty#SecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.security_group

SecurityGroups: TypeAlias = list["capo_guardduty.types.security_group.SecurityGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroups) -> list:
    import capo_guardduty.types.security_group

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.security_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityGroups:
    import capo_guardduty.types.security_group

    out: SecurityGroups = []
    for item in data:
        out.append(capo_guardduty.types.security_group.deserialize_json(item))
    return out
