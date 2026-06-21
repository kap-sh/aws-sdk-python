"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryLanguage``."""

from typing import Literal, TypeAlias, cast

QueryLanguage: TypeAlias = Literal[
    "CWLI",
    "SQL",
    "PPL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryLanguage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryLanguage:
    return cast(QueryLanguage, data)
