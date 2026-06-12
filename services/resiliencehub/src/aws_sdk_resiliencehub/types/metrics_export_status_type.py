"""Generated from Smithy shape ``com.amazonaws.resiliencehub#MetricsExportStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

MetricsExportStatusType: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Failed",
        "Success",
    )
)


def serialize_json(value: MetricsExportStatusType) -> str:
    return value


def deserialize_json(data: str) -> MetricsExportStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricsExportStatusType value: {data!r}")
    return cast(MetricsExportStatusType, data)
