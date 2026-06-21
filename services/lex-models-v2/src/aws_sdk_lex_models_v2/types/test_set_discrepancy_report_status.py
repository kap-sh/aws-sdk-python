"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetDiscrepancyReportStatus``."""

from typing import Literal, TypeAlias, cast

TestSetDiscrepancyReportStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSetDiscrepancyReportStatus) -> str:
    return value


def deserialize_json(data: str) -> TestSetDiscrepancyReportStatus:
    return cast(TestSetDiscrepancyReportStatus, data)
