"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewFilterBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProductViewFilterBy: TypeAlias = Literal[
    "FullTextSearch",
    "Owner",
    "ProductType",
    "SourceProductId",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FullTextSearch",
        "Owner",
        "ProductType",
        "SourceProductId",
    )
)


def serialize_aws_json_1_1(value: ProductViewFilterBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductViewFilterBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProductViewFilterBy value: {data!r}")
    return cast(ProductViewFilterBy, data)
