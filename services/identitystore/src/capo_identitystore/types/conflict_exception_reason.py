"""Generated from Smithy shape ``com.amazonaws.identitystore#ConflictExceptionReason``."""

from typing import Literal, TypeAlias, cast

ConflictExceptionReason: TypeAlias = Literal[
    "UNIQUENESS_CONSTRAINT_VIOLATION",
    "CONCURRENT_MODIFICATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConflictExceptionReason:
    return cast(ConflictExceptionReason, data)
