"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

ServiceJobType: TypeAlias = Literal["SAGEMAKER_TRAINING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SAGEMAKER_TRAINING",))


def serialize_json(value: ServiceJobType) -> str:
    return value


def deserialize_json(data: str) -> ServiceJobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceJobType value: {data!r}")
    return cast(ServiceJobType, data)
