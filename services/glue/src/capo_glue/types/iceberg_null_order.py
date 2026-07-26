"""Generated from Smithy shape ``com.amazonaws.glue#IcebergNullOrder``."""

from typing import Literal, TypeAlias, cast

IcebergNullOrder: TypeAlias = Literal[
    "nulls-first",
    "nulls-last",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergNullOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergNullOrder:
    return cast(IcebergNullOrder, data)
