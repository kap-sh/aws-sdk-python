"""Generated from Smithy shape ``com.amazonaws.cognitosync#DatasetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_sync.types.dataset

DatasetList: TypeAlias = list["capo_cognito_sync.types.dataset.Dataset"]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetList) -> list:
    import capo_cognito_sync.types.dataset

    out: list = []
    for item in value:
        out.append(capo_cognito_sync.types.dataset.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasetList:
    import capo_cognito_sync.types.dataset

    out: DatasetList = []
    for item in data:
        out.append(capo_cognito_sync.types.dataset.deserialize_json(item))
    return out
