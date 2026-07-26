"""Generated from Smithy shape ``com.amazonaws.securityhub#ActionTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.action_target

ActionTargetList: TypeAlias = list["capo_securityhub.types.action_target.ActionTarget"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionTargetList) -> list:
    import capo_securityhub.types.action_target

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.action_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionTargetList:
    import capo_securityhub.types.action_target

    out: ActionTargetList = []
    for item in data:
        out.append(capo_securityhub.types.action_target.deserialize_json(item))
    return out
