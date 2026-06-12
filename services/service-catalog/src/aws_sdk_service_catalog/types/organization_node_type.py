"""Generated from Smithy shape ``com.amazonaws.servicecatalog#OrganizationNodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

OrganizationNodeType: TypeAlias = Literal[
    "ORGANIZATION",
    "ORGANIZATIONAL_UNIT",
    "ACCOUNT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORGANIZATION",
        "ORGANIZATIONAL_UNIT",
        "ACCOUNT",
    )
)


def serialize_aws_json_1_1(value: OrganizationNodeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationNodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrganizationNodeType value: {data!r}")
    return cast(OrganizationNodeType, data)
