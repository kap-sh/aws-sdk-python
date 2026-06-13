"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobAnalysisType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ProtectedJobAnalysisType: TypeAlias = Literal["DIRECT_ANALYSIS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DIRECT_ANALYSIS",))


def serialize_json(value: ProtectedJobAnalysisType) -> str:
    return value


def deserialize_json(data: str) -> ProtectedJobAnalysisType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProtectedJobAnalysisType value: {data!r}")
    return cast(ProtectedJobAnalysisType, data)
