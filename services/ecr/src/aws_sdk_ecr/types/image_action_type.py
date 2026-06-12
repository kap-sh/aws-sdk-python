"""Generated from Smithy shape ``com.amazonaws.ecr#ImageActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ImageActionType: TypeAlias = Literal[
    "EXPIRE",
    "TRANSITION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXPIRE",
        "TRANSITION",
    )
)


def serialize_aws_json_1_1(value: ImageActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageActionType value: {data!r}")
    return cast(ImageActionType, data)
