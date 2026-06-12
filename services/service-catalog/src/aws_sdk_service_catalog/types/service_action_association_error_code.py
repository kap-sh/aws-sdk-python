"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionAssociationErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ServiceActionAssociationErrorCode: TypeAlias = Literal[
    "DUPLICATE_RESOURCE",
    "INTERNAL_FAILURE",
    "LIMIT_EXCEEDED",
    "RESOURCE_NOT_FOUND",
    "THROTTLING",
    "INVALID_PARAMETER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DUPLICATE_RESOURCE",
        "INTERNAL_FAILURE",
        "LIMIT_EXCEEDED",
        "RESOURCE_NOT_FOUND",
        "THROTTLING",
        "INVALID_PARAMETER",
    )
)


def serialize_aws_json_1_1(value: ServiceActionAssociationErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceActionAssociationErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceActionAssociationErrorCode value: {data!r}"
        )
    return cast(ServiceActionAssociationErrorCode, data)
