"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

ExtractionJobStatus: TypeAlias = Literal["FAILED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FAILED",))


def serialize_json(value: ExtractionJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ExtractionJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExtractionJobStatus value: {data!r}")
    return cast(ExtractionJobStatus, data)
