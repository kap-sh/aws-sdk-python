"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelInputDataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

ModelInputDataFormat: TypeAlias = Literal[
    "TEXT_CSV",
    "APPLICATION_JSON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT_CSV",
        "APPLICATION_JSON",
    )
)


def serialize_aws_json_1_1(value: ModelInputDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelInputDataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelInputDataFormat value: {data!r}")
    return cast(ModelInputDataFormat, data)
