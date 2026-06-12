"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviewCommentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DocumentReviewCommentType: TypeAlias = Literal["Comment",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Comment",))


def serialize_aws_json_1_1(value: DocumentReviewCommentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReviewCommentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentReviewCommentType value: {data!r}")
    return cast(DocumentReviewCommentType, data)
