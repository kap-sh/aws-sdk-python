"""Generated from Smithy shape ``com.amazonaws.athena#QueryResultType``."""

from typing import Literal, TypeAlias, cast

QueryResultType: TypeAlias = Literal[
    "DATA_MANIFEST",
    "DATA_ROWS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResultType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryResultType:
    return cast(QueryResultType, data)
