"""Generated from Smithy shape ``com.amazonaws.synthetics#DependencyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

DependencyType: TypeAlias = Literal["LambdaLayer",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LambdaLayer",))


def serialize_json(value: DependencyType) -> str:
    return value


def deserialize_json(data: str) -> DependencyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DependencyType value: {data!r}")
    return cast(DependencyType, data)
