"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJobStatus``."""

from typing import Literal, TypeAlias, cast

ExtractionJobStatus: TypeAlias = Literal["FAILED",]


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ExtractionJobStatus:
    return cast(ExtractionJobStatus, data)
