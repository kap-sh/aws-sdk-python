"""Generated from Smithy shape ``com.amazonaws.signer#Category``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_signer.errors import DeserializationError

Category: TypeAlias = Literal["AWSIoT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWSIoT",))


def serialize_json(value: Category) -> str:
    return value


def deserialize_json(data: str) -> Category:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Category value: {data!r}")
    return cast(Category, data)
