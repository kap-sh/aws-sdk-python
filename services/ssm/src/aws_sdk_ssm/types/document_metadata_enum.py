"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentMetadataEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DocumentMetadataEnum: TypeAlias = Literal["DocumentReviews",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DocumentReviews",))


def serialize_aws_json_1_1(value: DocumentMetadataEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentMetadataEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentMetadataEnum value: {data!r}")
    return cast(DocumentMetadataEnum, data)
