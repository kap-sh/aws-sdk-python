"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportSortAttribute``."""

from typing import Literal, TypeAlias, cast

ImportSortAttribute: TypeAlias = Literal["LastUpdatedDateTime",]


# --- restJson1 ser/de ---
def serialize_json(value: ImportSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> ImportSortAttribute:
    return cast(ImportSortAttribute, data)
