"""Generated from Smithy shape ``com.amazonaws.kendra#IndexStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

IndexStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "UPDATING",
    "SYSTEM_UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
        "UPDATING",
        "SYSTEM_UPDATING",
    )
)


def serialize_aws_json_1_1(value: IndexStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IndexStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndexStatus value: {data!r}")
    return cast(IndexStatus, data)
