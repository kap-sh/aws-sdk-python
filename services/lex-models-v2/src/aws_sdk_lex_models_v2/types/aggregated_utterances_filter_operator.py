"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AggregatedUtterancesFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AggregatedUtterancesFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CO",
        "EQ",
    )
)


def serialize_json(value: AggregatedUtterancesFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> AggregatedUtterancesFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AggregatedUtterancesFilterOperator value: {data!r}"
        )
    return cast(AggregatedUtterancesFilterOperator, data)
