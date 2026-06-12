"""Generated from Smithy shape ``com.amazonaws.batch#ServiceResourceIdName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

ServiceResourceIdName: TypeAlias = Literal["TrainingJobArn",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TrainingJobArn",))


def serialize_json(value: ServiceResourceIdName) -> str:
    return value


def deserialize_json(data: str) -> ServiceResourceIdName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceResourceIdName value: {data!r}")
    return cast(ServiceResourceIdName, data)
