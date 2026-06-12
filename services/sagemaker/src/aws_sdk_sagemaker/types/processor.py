"""Generated from Smithy shape ``com.amazonaws.sagemaker#Processor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

Processor: TypeAlias = Literal[
    "CPU",
    "GPU",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPU",
        "GPU",
    )
)


def serialize_aws_json_1_1(value: Processor) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Processor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Processor value: {data!r}")
    return cast(Processor, data)
