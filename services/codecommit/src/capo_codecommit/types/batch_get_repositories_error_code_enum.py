"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetRepositoriesErrorCodeEnum``."""

from typing import Literal, TypeAlias, cast

BatchGetRepositoriesErrorCodeEnum: TypeAlias = Literal[
    "EncryptionIntegrityChecksFailedException",
    "EncryptionKeyAccessDeniedException",
    "EncryptionKeyDisabledException",
    "EncryptionKeyNotFoundException",
    "EncryptionKeyUnavailableException",
    "RepositoryDoesNotExistException",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetRepositoriesErrorCodeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchGetRepositoriesErrorCodeEnum:
    return cast(BatchGetRepositoriesErrorCodeEnum, data)
