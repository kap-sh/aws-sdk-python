"""Generated from Smithy shape ``com.amazonaws.neptunegraph#MultiValueHandlingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

MultiValueHandlingType: TypeAlias = Literal[
    "TO_LIST",
    "PICK_FIRST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TO_LIST",
        "PICK_FIRST",
    )
)


def serialize_json(value: MultiValueHandlingType) -> str:
    return value


def deserialize_json(data: str) -> MultiValueHandlingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MultiValueHandlingType value: {data!r}")
    return cast(MultiValueHandlingType, data)
