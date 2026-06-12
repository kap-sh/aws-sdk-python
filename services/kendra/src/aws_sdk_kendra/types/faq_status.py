"""Generated from Smithy shape ``com.amazonaws.kendra#FaqStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

FaqStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: FaqStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FaqStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FaqStatus value: {data!r}")
    return cast(FaqStatus, data)
