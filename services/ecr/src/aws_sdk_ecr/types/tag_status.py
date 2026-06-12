"""Generated from Smithy shape ``com.amazonaws.ecr#TagStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

TagStatus: TypeAlias = Literal[
    "TAGGED",
    "UNTAGGED",
    "ANY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TAGGED",
        "UNTAGGED",
        "ANY",
    )
)


def serialize_aws_json_1_1(value: TagStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TagStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TagStatus value: {data!r}")
    return cast(TagStatus, data)
