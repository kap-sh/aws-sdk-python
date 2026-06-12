"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProductViewSortBy: TypeAlias = Literal[
    "Title",
    "VersionCount",
    "CreationDate",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Title",
        "VersionCount",
        "CreationDate",
    )
)


def serialize_aws_json_1_1(value: ProductViewSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductViewSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProductViewSortBy value: {data!r}")
    return cast(ProductViewSortBy, data)
