"""Generated from Smithy shape ``com.amazonaws.neptunedata#StatisticsAutoGenerationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

StatisticsAutoGenerationMode: TypeAlias = Literal[
    "disableAutoCompute",
    "enableAutoCompute",
    "refresh",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disableAutoCompute",
        "enableAutoCompute",
        "refresh",
    )
)


def serialize_json(value: StatisticsAutoGenerationMode) -> str:
    return value


def deserialize_json(data: str) -> StatisticsAutoGenerationMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StatisticsAutoGenerationMode value: {data!r}"
        )
    return cast(StatisticsAutoGenerationMode, data)
