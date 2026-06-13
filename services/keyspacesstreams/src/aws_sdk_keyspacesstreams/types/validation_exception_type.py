"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ValidationExceptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_keyspacesstreams.errors import DeserializationError

ValidationExceptionType: TypeAlias = Literal[
    "InvalidFormat",
    "TrimmedDataAccess",
    "ExpiredIterator",
    "ExpiredNextToken",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvalidFormat",
        "TrimmedDataAccess",
        "ExpiredIterator",
        "ExpiredNextToken",
    )
)


def serialize_aws_json_1_0(value: ValidationExceptionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionType value: {data!r}")
    return cast(ValidationExceptionType, data)
