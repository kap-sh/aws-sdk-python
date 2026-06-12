"""Generated from Smithy shape ``com.amazonaws.firehose#NoEncryptionConfig``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

NoEncryptionConfig: TypeAlias = Literal["NoEncryption",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NoEncryption",))


def serialize_aws_json_1_1(value: NoEncryptionConfig) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NoEncryptionConfig:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NoEncryptionConfig value: {data!r}")
    return cast(NoEncryptionConfig, data)
