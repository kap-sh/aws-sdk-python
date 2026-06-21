"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductSource``."""

from typing import Literal, TypeAlias, cast

ProductSource: TypeAlias = Literal["ACCOUNT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductSource:
    return cast(ProductSource, data)
