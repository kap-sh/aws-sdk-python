"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AdditionalInfoValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.string1024

AdditionalInfoValueList: TypeAlias = list[
    "capo_resiliencehub.types.string1024.String1024"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalInfoValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> AdditionalInfoValueList:
    return list(data)
