"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagMutability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ImageTagMutability: TypeAlias = Literal[
    "MUTABLE",
    "IMMUTABLE",
    "IMMUTABLE_WITH_EXCLUSION",
    "MUTABLE_WITH_EXCLUSION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MUTABLE",
        "IMMUTABLE",
        "IMMUTABLE_WITH_EXCLUSION",
        "MUTABLE_WITH_EXCLUSION",
    )
)


def serialize_aws_json_1_1(value: ImageTagMutability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageTagMutability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageTagMutability value: {data!r}")
    return cast(ImageTagMutability, data)
