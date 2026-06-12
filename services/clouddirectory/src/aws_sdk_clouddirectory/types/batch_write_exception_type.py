"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteExceptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

BatchWriteExceptionType: TypeAlias = Literal[
    "InternalServiceException",
    "ValidationException",
    "InvalidArnException",
    "LinkNameAlreadyInUseException",
    "StillContainsLinksException",
    "FacetValidationException",
    "ObjectNotDetachedException",
    "ResourceNotFoundException",
    "AccessDeniedException",
    "InvalidAttachmentException",
    "NotIndexException",
    "NotNodeException",
    "IndexedAttributeMissingException",
    "ObjectAlreadyDetachedException",
    "NotPolicyException",
    "DirectoryNotEnabledException",
    "LimitExceededException",
    "UnsupportedIndexTypeException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InternalServiceException",
        "ValidationException",
        "InvalidArnException",
        "LinkNameAlreadyInUseException",
        "StillContainsLinksException",
        "FacetValidationException",
        "ObjectNotDetachedException",
        "ResourceNotFoundException",
        "AccessDeniedException",
        "InvalidAttachmentException",
        "NotIndexException",
        "NotNodeException",
        "IndexedAttributeMissingException",
        "ObjectAlreadyDetachedException",
        "NotPolicyException",
        "DirectoryNotEnabledException",
        "LimitExceededException",
        "UnsupportedIndexTypeException",
    )
)


def serialize_json(value: BatchWriteExceptionType) -> str:
    return value


def deserialize_json(data: str) -> BatchWriteExceptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchWriteExceptionType value: {data!r}")
    return cast(BatchWriteExceptionType, data)
