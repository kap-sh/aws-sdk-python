"""Generated from Smithy shape ``com.amazonaws.ecr#TargetStorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

TargetStorageClass: TypeAlias = Literal[
    "STANDARD",
    "ARCHIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "ARCHIVE",
    )
)


def serialize_aws_json_1_1(value: TargetStorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetStorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetStorageClass value: {data!r}")
    return cast(TargetStorageClass, data)
