"""Generated from Smithy shape ``com.amazonaws.lakeformation#AuthorizedSessionTagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.name_string

AuthorizedSessionTagValueList: TypeAlias = list[
    "capo_lakeformation.types.name_string.NameString"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizedSessionTagValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> AuthorizedSessionTagValueList:
    return list(data)
