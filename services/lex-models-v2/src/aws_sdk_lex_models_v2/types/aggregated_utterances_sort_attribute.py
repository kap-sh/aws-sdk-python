"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AggregatedUtterancesSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AggregatedUtterancesSortAttribute: TypeAlias = Literal[
    "HitCount",
    "MissedCount",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HitCount",
        "MissedCount",
    )
)


def serialize_json(value: AggregatedUtterancesSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> AggregatedUtterancesSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AggregatedUtterancesSortAttribute value: {data!r}"
        )
    return cast(AggregatedUtterancesSortAttribute, data)
