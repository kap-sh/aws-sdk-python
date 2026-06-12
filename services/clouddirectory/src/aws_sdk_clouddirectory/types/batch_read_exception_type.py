"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadExceptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

BatchReadExceptionType: TypeAlias = Literal[
    "ValidationException",
    "InvalidArnException",
    "ResourceNotFoundException",
    "InvalidNextTokenException",
    "AccessDeniedException",
    "NotNodeException",
    "FacetValidationException",
    "CannotListParentOfRootException",
    "NotIndexException",
    "NotPolicyException",
    "DirectoryNotEnabledException",
    "LimitExceededException",
    "InternalServiceException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ValidationException",
        "InvalidArnException",
        "ResourceNotFoundException",
        "InvalidNextTokenException",
        "AccessDeniedException",
        "NotNodeException",
        "FacetValidationException",
        "CannotListParentOfRootException",
        "NotIndexException",
        "NotPolicyException",
        "DirectoryNotEnabledException",
        "LimitExceededException",
        "InternalServiceException",
    )
)


def serialize_json(value: BatchReadExceptionType) -> str:
    return value


def deserialize_json(data: str) -> BatchReadExceptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchReadExceptionType value: {data!r}")
    return cast(BatchReadExceptionType, data)
