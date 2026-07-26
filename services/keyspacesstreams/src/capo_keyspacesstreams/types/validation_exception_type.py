"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ValidationExceptionType``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionType: TypeAlias = Literal[
    "InvalidFormat",
    "TrimmedDataAccess",
    "ExpiredIterator",
    "ExpiredNextToken",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionType:
    return cast(ValidationExceptionType, data)
