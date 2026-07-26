"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#TargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.target

TargetList: TypeAlias = list["capo_chime_sdk_messaging.types.target.Target"]


# --- restJson1 ser/de ---
def serialize_json(value: TargetList) -> list:
    import capo_chime_sdk_messaging.types.target

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_messaging.types.target.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetList:
    import capo_chime_sdk_messaging.types.target

    out: TargetList = []
    for item in data:
        out.append(capo_chime_sdk_messaging.types.target.deserialize_json(item))
    return out
