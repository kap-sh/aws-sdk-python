"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateValidationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AnalysisTemplateValidationType: TypeAlias = Literal["DIFFERENTIAL_PRIVACY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DIFFERENTIAL_PRIVACY",))


def serialize_json(value: AnalysisTemplateValidationType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisTemplateValidationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalysisTemplateValidationType value: {data!r}"
        )
    return cast(AnalysisTemplateValidationType, data)
