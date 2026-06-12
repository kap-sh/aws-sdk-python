"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyStorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

LifecyclePolicyStorageClass: TypeAlias = Literal[
    "ARCHIVE",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARCHIVE",
        "STANDARD",
    )
)


def serialize_aws_json_1_1(value: LifecyclePolicyStorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecyclePolicyStorageClass:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LifecyclePolicyStorageClass value: {data!r}"
        )
    return cast(LifecyclePolicyStorageClass, data)
