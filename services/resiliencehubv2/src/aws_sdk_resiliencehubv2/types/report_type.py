"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportType``."""

from typing import Literal, TypeAlias, cast

ReportType: TypeAlias = Literal["FAILURE_MODE",]


# --- restJson1 ser/de ---
def serialize_json(value: ReportType) -> str:
    return value


def deserialize_json(data: str) -> ReportType:
    return cast(ReportType, data)
