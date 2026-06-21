"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportFilterName``."""

from typing import Literal, TypeAlias, cast

ExportFilterName: TypeAlias = Literal["ExportResourceType",]


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilterName) -> str:
    return value


def deserialize_json(data: str) -> ExportFilterName:
    return cast(ExportFilterName, data)
