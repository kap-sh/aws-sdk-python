"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service_data.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "INVALID_REALM",
    "INVALID_DIRECTORY_TYPE",
    "INVALID_SECONDARY_REGION",
    "INVALID_NEXT_TOKEN",
    "INVALID_ATTRIBUTE_VALUE",
    "INVALID_ATTRIBUTE_NAME",
    "INVALID_ATTRIBUTE_FOR_USER",
    "INVALID_ATTRIBUTE_FOR_GROUP",
    "INVALID_ATTRIBUTE_FOR_SEARCH",
    "INVALID_ATTRIBUTE_FOR_MODIFY",
    "DUPLICATE_ATTRIBUTE",
    "MISSING_ATTRIBUTE",
    "ATTRIBUTE_EXISTS",
    "LDAP_SIZE_LIMIT_EXCEEDED",
    "LDAP_UNSUPPORTED_OPERATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_REALM",
        "INVALID_DIRECTORY_TYPE",
        "INVALID_SECONDARY_REGION",
        "INVALID_NEXT_TOKEN",
        "INVALID_ATTRIBUTE_VALUE",
        "INVALID_ATTRIBUTE_NAME",
        "INVALID_ATTRIBUTE_FOR_USER",
        "INVALID_ATTRIBUTE_FOR_GROUP",
        "INVALID_ATTRIBUTE_FOR_SEARCH",
        "INVALID_ATTRIBUTE_FOR_MODIFY",
        "DUPLICATE_ATTRIBUTE",
        "MISSING_ATTRIBUTE",
        "ATTRIBUTE_EXISTS",
        "LDAP_SIZE_LIMIT_EXCEEDED",
        "LDAP_UNSUPPORTED_OPERATION",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
