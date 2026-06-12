"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProductType: TypeAlias = Literal[
    "CLOUD_FORMATION_TEMPLATE",
    "MARKETPLACE",
    "TERRAFORM_OPEN_SOURCE",
    "TERRAFORM_CLOUD",
    "EXTERNAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUD_FORMATION_TEMPLATE",
        "MARKETPLACE",
        "TERRAFORM_OPEN_SOURCE",
        "TERRAFORM_CLOUD",
        "EXTERNAL",
    )
)


def serialize_aws_json_1_1(value: ProductType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProductType value: {data!r}")
    return cast(ProductType, data)
