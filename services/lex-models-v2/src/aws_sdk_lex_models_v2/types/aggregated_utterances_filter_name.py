"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AggregatedUtterancesFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AggregatedUtterancesFilterName: TypeAlias = Literal["Utterance",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Utterance",))


def serialize_json(value: AggregatedUtterancesFilterName) -> str:
    return value


def deserialize_json(data: str) -> AggregatedUtterancesFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AggregatedUtterancesFilterName value: {data!r}"
        )
    return cast(AggregatedUtterancesFilterName, data)
