"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfFindingType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.finding_type

__listOfFindingType: TypeAlias = list["capo_macie2.types.finding_type.FindingType"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFindingType) -> list:
    import capo_macie2.types.finding_type

    out: list = []
    for item in value:
        out.append(capo_macie2.types.finding_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFindingType:
    import capo_macie2.types.finding_type

    out: __listOfFindingType = []
    for item in data:
        out.append(capo_macie2.types.finding_type.deserialize_json(item))
    return out
