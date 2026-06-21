"""Generated from Smithy shape ``com.amazonaws.organizations#AccessDeniedForDependencyExceptionReason``."""

from typing import Literal, TypeAlias, cast

AccessDeniedForDependencyExceptionReason: TypeAlias = Literal[
    "ACCESS_DENIED_DURING_CREATE_SERVICE_LINKED_ROLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedForDependencyExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessDeniedForDependencyExceptionReason:
    return cast(AccessDeniedForDependencyExceptionReason, data)
