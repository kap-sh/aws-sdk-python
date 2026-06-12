"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ContainerType: TypeAlias = Literal["DOCKER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DOCKER",))


def serialize_json(value: ContainerType) -> str:
    return value


def deserialize_json(data: str) -> ContainerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerType value: {data!r}")
    return cast(ContainerType, data)
