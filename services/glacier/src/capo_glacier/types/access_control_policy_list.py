"""Generated from Smithy shape ``com.amazonaws.glacier#AccessControlPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glacier.types.grant

AccessControlPolicyList: TypeAlias = list["capo_glacier.types.grant.Grant"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessControlPolicyList) -> list:
    import capo_glacier.types.grant

    out: list = []
    for item in value:
        out.append(capo_glacier.types.grant.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessControlPolicyList:
    import capo_glacier.types.grant

    out: AccessControlPolicyList = []
    for item in data:
        out.append(capo_glacier.types.grant.deserialize_json(item))
    return out
