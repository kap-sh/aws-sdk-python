"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

LifecyclePolicyDetailFilterType: TypeAlias = Literal[
    "AGE",
    "COUNT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGE",
        "COUNT",
    )
)


def serialize_json(value: LifecyclePolicyDetailFilterType) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyDetailFilterType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LifecyclePolicyDetailFilterType value: {data!r}"
        )
    return cast(LifecyclePolicyDetailFilterType, data)
