"""Generated from Smithy shape ``com.amazonaws.comprehend#InvalidRequestReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

InvalidRequestReason: TypeAlias = Literal["INVALID_DOCUMENT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INVALID_DOCUMENT",))


def serialize_aws_json_1_1(value: InvalidRequestReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InvalidRequestReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvalidRequestReason value: {data!r}")
    return cast(InvalidRequestReason, data)
