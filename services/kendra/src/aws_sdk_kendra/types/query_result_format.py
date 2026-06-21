"""Generated from Smithy shape ``com.amazonaws.kendra#QueryResultFormat``."""

from typing import Literal, TypeAlias, cast

QueryResultFormat: TypeAlias = Literal[
    "TABLE",
    "TEXT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResultFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryResultFormat:
    return cast(QueryResultFormat, data)
