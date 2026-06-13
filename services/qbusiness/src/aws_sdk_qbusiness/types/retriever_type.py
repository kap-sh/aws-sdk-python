"""Generated from Smithy shape ``com.amazonaws.qbusiness#RetrieverType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

RetrieverType: TypeAlias = Literal[
    "NATIVE_INDEX",
    "KENDRA_INDEX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NATIVE_INDEX",
        "KENDRA_INDEX",
    )
)


def serialize_json(value: RetrieverType) -> str:
    return value


def deserialize_json(data: str) -> RetrieverType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetrieverType value: {data!r}")
    return cast(RetrieverType, data)
