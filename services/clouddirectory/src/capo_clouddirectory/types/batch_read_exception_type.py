"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadExceptionType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: BatchReadExceptionType) -> str:
    return value


def deserialize_json(data: str) -> BatchReadExceptionType:
    return cast(BatchReadExceptionType, data)
