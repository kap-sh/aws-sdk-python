"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableClass``."""

from typing import Literal, TypeAlias, cast

TableClass: TypeAlias = Literal[
    "STANDARD",
    "STANDARD_INFREQUENT_ACCESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableClass) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TableClass:
    return cast(TableClass, data)
