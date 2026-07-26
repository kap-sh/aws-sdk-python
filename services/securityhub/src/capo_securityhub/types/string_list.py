"""Generated from Smithy shape ``com.amazonaws.securityhub#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string

StringList: TypeAlias = list["capo_securityhub.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return list(data)
