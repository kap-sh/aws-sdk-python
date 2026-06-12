"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

ServiceEnvironmentType: TypeAlias = Literal["SAGEMAKER_TRAINING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SAGEMAKER_TRAINING",))


def serialize_json(value: ServiceEnvironmentType) -> str:
    return value


def deserialize_json(data: str) -> ServiceEnvironmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceEnvironmentType value: {data!r}")
    return cast(ServiceEnvironmentType, data)
