"""Generated from Smithy shape ``com.amazonaws.identitystore#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_identitystore.errors import DeserializationError

ConflictExceptionReason: TypeAlias = Literal[
    "UNIQUENESS_CONSTRAINT_VIOLATION",
    "CONCURRENT_MODIFICATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNIQUENESS_CONSTRAINT_VIOLATION",
        "CONCURRENT_MODIFICATION",
    )
)


def serialize_aws_json_1_1(value: ConflictExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConflictExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictExceptionReason value: {data!r}")
    return cast(ConflictExceptionReason, data)
