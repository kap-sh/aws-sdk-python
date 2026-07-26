"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSortDirection``."""

from typing import Literal, TypeAlias, cast

IcebergSortDirection: TypeAlias = Literal[
    "asc",
    "desc",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergSortDirection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergSortDirection:
    return cast(IcebergSortDirection, data)
