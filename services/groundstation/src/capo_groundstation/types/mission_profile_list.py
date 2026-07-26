"""Generated from Smithy shape ``com.amazonaws.groundstation#MissionProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.mission_profile_list_item

MissionProfileList: TypeAlias = list[
    "capo_groundstation.types.mission_profile_list_item.MissionProfileListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: MissionProfileList) -> list:
    import capo_groundstation.types.mission_profile_list_item

    out: list = []
    for item in value:
        out.append(
            capo_groundstation.types.mission_profile_list_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MissionProfileList:
    import capo_groundstation.types.mission_profile_list_item

    out: MissionProfileList = []
    for item in data:
        out.append(
            capo_groundstation.types.mission_profile_list_item.deserialize_json(item)
        )
    return out
