"""Generated from Smithy shape ``com.amazonaws.organizations#AccessDeniedForDependencyExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

AccessDeniedForDependencyExceptionReason: TypeAlias = Literal[
    "ACCESS_DENIED_DURING_CREATE_SERVICE_LINKED_ROLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    ("ACCESS_DENIED_DURING_CREATE_SERVICE_LINKED_ROLE",)
)


def serialize_aws_json_1_1(value: AccessDeniedForDependencyExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessDeniedForDependencyExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccessDeniedForDependencyExceptionReason value: {data!r}"
        )
    return cast(AccessDeniedForDependencyExceptionReason, data)
