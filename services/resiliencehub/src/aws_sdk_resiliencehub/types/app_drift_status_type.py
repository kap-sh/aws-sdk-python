"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppDriftStatusType``."""

from typing import Literal, TypeAlias, cast

AppDriftStatusType: TypeAlias = Literal[
    "NotChecked",
    "NotDetected",
    "Detected",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppDriftStatusType) -> str:
    return value


def deserialize_json(data: str) -> AppDriftStatusType:
    return cast(AppDriftStatusType, data)
