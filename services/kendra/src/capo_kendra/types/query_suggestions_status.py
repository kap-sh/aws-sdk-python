"""Generated from Smithy shape ``com.amazonaws.kendra#QuerySuggestionsStatus``."""

from typing import Literal, TypeAlias, cast

QuerySuggestionsStatus: TypeAlias = Literal[
    "ACTIVE",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuerySuggestionsStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QuerySuggestionsStatus:
    return cast(QuerySuggestionsStatus, data)
