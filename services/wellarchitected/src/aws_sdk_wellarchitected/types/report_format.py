"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReportFormat``."""

from typing import Literal, TypeAlias, cast

ReportFormat: TypeAlias = Literal[
    "PDF",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportFormat) -> str:
    return value


def deserialize_json(data: str) -> ReportFormat:
    return cast(ReportFormat, data)
