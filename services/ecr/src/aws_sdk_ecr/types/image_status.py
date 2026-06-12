"""Generated from Smithy shape ``com.amazonaws.ecr#ImageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ImageStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ACTIVATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ARCHIVED",
        "ACTIVATING",
    )
)


def serialize_aws_json_1_1(value: ImageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageStatus value: {data!r}")
    return cast(ImageStatus, data)
