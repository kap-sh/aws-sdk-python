"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelOutputDataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

ModelOutputDataFormat: TypeAlias = Literal[
    "TEXT_CSV",
    "APPLICATION_JSONLINES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT_CSV",
        "APPLICATION_JSONLINES",
    )
)


def serialize_aws_json_1_1(value: ModelOutputDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelOutputDataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelOutputDataFormat value: {data!r}")
    return cast(ModelOutputDataFormat, data)
