"""Generated from Smithy shape ``com.amazonaws.kendra#QueryResultType``."""

from typing import Literal, TypeAlias, cast

QueryResultType: TypeAlias = Literal[
    "DOCUMENT",
    "QUESTION_ANSWER",
    "ANSWER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResultType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryResultType:
    return cast(QueryResultType, data)
