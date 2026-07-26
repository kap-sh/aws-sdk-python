"""Generated from Smithy shape ``com.amazonaws.inspector2#ContinuousIntegrationScanEvent``."""

from typing import Literal, TypeAlias, cast

ContinuousIntegrationScanEvent: TypeAlias = Literal[
    "PULL_REQUEST",
    "PUSH",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContinuousIntegrationScanEvent) -> str:
    return value


def deserialize_json(data: str) -> ContinuousIntegrationScanEvent:
    return cast(ContinuousIntegrationScanEvent, data)
