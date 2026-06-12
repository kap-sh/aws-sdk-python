"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentHashType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AttachmentHashType: TypeAlias = Literal["Sha256",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Sha256",))


def serialize_aws_json_1_1(value: AttachmentHashType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttachmentHashType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentHashType value: {data!r}")
    return cast(AttachmentHashType, data)
