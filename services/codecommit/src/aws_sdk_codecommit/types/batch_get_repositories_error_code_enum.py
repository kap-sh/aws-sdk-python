"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetRepositoriesErrorCodeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

BatchGetRepositoriesErrorCodeEnum: TypeAlias = Literal[
    "EncryptionIntegrityChecksFailedException",
    "EncryptionKeyAccessDeniedException",
    "EncryptionKeyDisabledException",
    "EncryptionKeyNotFoundException",
    "EncryptionKeyUnavailableException",
    "RepositoryDoesNotExistException",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EncryptionIntegrityChecksFailedException",
        "EncryptionKeyAccessDeniedException",
        "EncryptionKeyDisabledException",
        "EncryptionKeyNotFoundException",
        "EncryptionKeyUnavailableException",
        "RepositoryDoesNotExistException",
    )
)


def serialize_aws_json_1_1(value: BatchGetRepositoriesErrorCodeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchGetRepositoriesErrorCodeEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchGetRepositoriesErrorCodeEnum value: {data!r}"
        )
    return cast(BatchGetRepositoriesErrorCodeEnum, data)
