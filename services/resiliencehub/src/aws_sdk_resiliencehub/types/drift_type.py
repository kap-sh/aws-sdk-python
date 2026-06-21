"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DriftType``."""

from typing import Literal, TypeAlias, cast

DriftType: TypeAlias = Literal[
    "ApplicationCompliance",
    "AppComponentResiliencyComplianceStatus",
]


# --- restJson1 ser/de ---
def serialize_json(value: DriftType) -> str:
    return value


def deserialize_json(data: str) -> DriftType:
    return cast(DriftType, data)
