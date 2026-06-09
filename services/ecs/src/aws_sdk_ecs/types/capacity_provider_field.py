"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

CapacityProviderField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TAGS",))


def serialize_aws_json_1_1(value: CapacityProviderField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityProviderField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityProviderField value: {data!r}")
    return cast(CapacityProviderField, data)
