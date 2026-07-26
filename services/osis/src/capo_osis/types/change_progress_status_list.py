"""Generated from Smithy shape ``com.amazonaws.osis#ChangeProgressStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_osis.types.change_progress_status

ChangeProgressStatusList: TypeAlias = list[
    "capo_osis.types.change_progress_status.ChangeProgressStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStatusList) -> list:
    import capo_osis.types.change_progress_status

    out: list = []
    for item in value:
        out.append(capo_osis.types.change_progress_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeProgressStatusList:
    import capo_osis.types.change_progress_status

    out: ChangeProgressStatusList = []
    for item in data:
        out.append(capo_osis.types.change_progress_status.deserialize_json(item))
    return out
