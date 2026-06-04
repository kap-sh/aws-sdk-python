"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceField``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ServiceField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TAGS",))


def serialize_aws_json_1_1(value: ServiceField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceField value: {data!r}")
    return cast(ServiceField, data)
