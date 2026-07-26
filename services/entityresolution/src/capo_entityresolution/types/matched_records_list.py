"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchedRecordsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.matched_record

MatchedRecordsList: TypeAlias = list[
    "capo_entityresolution.types.matched_record.MatchedRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchedRecordsList) -> list:
    import capo_entityresolution.types.matched_record

    out: list = []
    for item in value:
        out.append(capo_entityresolution.types.matched_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchedRecordsList:
    import capo_entityresolution.types.matched_record

    out: MatchedRecordsList = []
    for item in data:
        out.append(capo_entityresolution.types.matched_record.deserialize_json(item))
    return out
