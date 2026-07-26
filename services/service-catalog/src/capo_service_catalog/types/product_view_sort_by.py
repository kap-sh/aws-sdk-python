"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewSortBy``."""

from typing import Literal, TypeAlias, cast

ProductViewSortBy: TypeAlias = Literal[
    "Title",
    "VersionCount",
    "CreationDate",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductViewSortBy:
    return cast(ProductViewSortBy, data)
