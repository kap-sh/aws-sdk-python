"""Generated from Smithy shape ``com.amazonaws.resiliencehub#MetricsExportStatusType``."""

from typing import Literal, TypeAlias, cast

MetricsExportStatusType: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricsExportStatusType) -> str:
    return value


def deserialize_json(data: str) -> MetricsExportStatusType:
    return cast(MetricsExportStatusType, data)
