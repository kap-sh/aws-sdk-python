"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportSortAttribute``."""

from typing import Literal, TypeAlias, cast

ExportSortAttribute: TypeAlias = Literal["LastUpdatedDateTime",]


# --- restJson1 ser/de ---
def serialize_json(value: ExportSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> ExportSortAttribute:
    return cast(ExportSortAttribute, data)
