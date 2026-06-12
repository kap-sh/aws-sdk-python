"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MergeStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

MergeStrategy: TypeAlias = Literal[
    "OVERWRITE_LATEST",
    "FAIL_ON_CONFLICT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OVERWRITE_LATEST",
        "FAIL_ON_CONFLICT",
    )
)


def serialize_json(value: MergeStrategy) -> str:
    return value


def deserialize_json(data: str) -> MergeStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MergeStrategy value: {data!r}")
    return cast(MergeStrategy, data)
