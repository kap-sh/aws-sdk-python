"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

ModelSource: TypeAlias = Literal["SAGEMAKER",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SAGEMAKER",))


def serialize_aws_json_1_1(value: ModelSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelSource value: {data!r}")
    return cast(ModelSource, data)
