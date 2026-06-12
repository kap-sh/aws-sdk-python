"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetDiscrepancyReportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestSetDiscrepancyReportStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
    )
)


def serialize_json(value: TestSetDiscrepancyReportStatus) -> str:
    return value


def deserialize_json(data: str) -> TestSetDiscrepancyReportStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TestSetDiscrepancyReportStatus value: {data!r}"
        )
    return cast(TestSetDiscrepancyReportStatus, data)
