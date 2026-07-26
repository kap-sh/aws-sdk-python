"""Generated from Smithy shape ``com.amazonaws.datazone#PolicyGrantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.policy_grant_member

PolicyGrantList: TypeAlias = list[
    "capo_datazone.types.policy_grant_member.PolicyGrantMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGrantList) -> list:
    import capo_datazone.types.policy_grant_member

    out: list = []
    for item in value:
        out.append(capo_datazone.types.policy_grant_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyGrantList:
    import capo_datazone.types.policy_grant_member

    out: PolicyGrantList = []
    for item in data:
        out.append(capo_datazone.types.policy_grant_member.deserialize_json(item))
    return out
