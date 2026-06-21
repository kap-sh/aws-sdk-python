"""Generated from Smithy shape ``com.amazonaws.kendra#QueryIdentifiersEnclosingOption``."""

from typing import Literal, TypeAlias, cast

QueryIdentifiersEnclosingOption: TypeAlias = Literal[
    "DOUBLE_QUOTES",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryIdentifiersEnclosingOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryIdentifiersEnclosingOption:
    return cast(QueryIdentifiersEnclosingOption, data)
