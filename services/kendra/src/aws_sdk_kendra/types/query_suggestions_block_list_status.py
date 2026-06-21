"""Generated from Smithy shape ``com.amazonaws.kendra#QuerySuggestionsBlockListStatus``."""

from typing import Literal, TypeAlias, cast

QuerySuggestionsBlockListStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "DELETING",
    "UPDATING",
    "ACTIVE_BUT_UPDATE_FAILED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuerySuggestionsBlockListStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QuerySuggestionsBlockListStatus:
    return cast(QuerySuggestionsBlockListStatus, data)
