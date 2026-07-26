"""Generated from Smithy shape ``com.amazonaws.wickr#SecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.security_group

SecurityGroupList: TypeAlias = list["capo_wickr.types.security_group.SecurityGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupList) -> list:
    import capo_wickr.types.security_group

    out: list = []
    for item in value:
        out.append(capo_wickr.types.security_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityGroupList:
    import capo_wickr.types.security_group

    out: SecurityGroupList = []
    for item in data:
        out.append(capo_wickr.types.security_group.deserialize_json(item))
    return out
