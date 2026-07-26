"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteExceptionType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: BatchWriteExceptionType) -> str:
    return value


def deserialize_json(data: str) -> BatchWriteExceptionType:
    return cast(BatchWriteExceptionType, data)
