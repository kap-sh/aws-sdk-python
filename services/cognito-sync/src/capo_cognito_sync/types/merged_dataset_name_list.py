"""Generated from Smithy shape ``com.amazonaws.cognitosync#MergedDatasetNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_sync.types.string

MergedDatasetNameList: TypeAlias = list["capo_cognito_sync.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: MergedDatasetNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> MergedDatasetNameList:
    return list(data)
