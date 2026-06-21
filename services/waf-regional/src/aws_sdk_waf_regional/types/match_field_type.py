"""Generated from Smithy shape ``com.amazonaws.wafregional#MatchFieldType``."""

from typing import Literal, TypeAlias, cast

MatchFieldType: TypeAlias = Literal[
    "URI",
    "QUERY_STRING",
    "HEADER",
    "METHOD",
    "BODY",
    "SINGLE_QUERY_ARG",
    "ALL_QUERY_ARGS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchFieldType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MatchFieldType:
    return cast(MatchFieldType, data)
