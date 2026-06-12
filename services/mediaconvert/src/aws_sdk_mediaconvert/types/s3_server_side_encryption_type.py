"""Generated from Smithy shape ``com.amazonaws.mediaconvert#S3ServerSideEncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify how you want your data keys managed. AWS uses data keys to encrypt your content. AWS also encrypts the data keys themselves, using a customer master key (CMK), and then stores the encrypted data keys alongside your encrypted content. Use this setting to specify which AWS service manages the CMK. For simplest set up, choose Amazon S3. If you want your master key to be managed by AWS Key Management Service (KMS), choose AWS KMS. By default, when you choose AWS KMS, KMS uses the AWS managed customer master key (CMK) associated with Amazon S3 to encrypt your data keys. You can optionally choose to specify a different, customer managed CMK. Do so by specifying the Amazon Resource Name (ARN) of the key for the setting KMS ARN."""
S3ServerSideEncryptionType: TypeAlias = Literal[
    "SERVER_SIDE_ENCRYPTION_S3",
    "SERVER_SIDE_ENCRYPTION_KMS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVER_SIDE_ENCRYPTION_S3",
        "SERVER_SIDE_ENCRYPTION_KMS",
    )
)


def serialize_json(value: S3ServerSideEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> S3ServerSideEncryptionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown S3ServerSideEncryptionType value: {data!r}"
        )
    return cast(S3ServerSideEncryptionType, data)
