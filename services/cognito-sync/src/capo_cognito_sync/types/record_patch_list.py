"""Generated from Smithy shape ``com.amazonaws.cognitosync#RecordPatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_sync.types.record_patch

RecordPatchList: TypeAlias = list["capo_cognito_sync.types.record_patch.RecordPatch"]


# --- restJson1 ser/de ---
def serialize_json(value: RecordPatchList) -> list:
    import capo_cognito_sync.types.record_patch

    out: list = []
    for item in value:
        out.append(capo_cognito_sync.types.record_patch.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecordPatchList:
    import capo_cognito_sync.types.record_patch

    out: RecordPatchList = []
    for item in data:
        out.append(capo_cognito_sync.types.record_patch.deserialize_json(item))
    return out
