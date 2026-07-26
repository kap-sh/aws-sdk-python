"""Generated from Smithy shape ``com.amazonaws.kendra#AttributeSuggestionsMode``."""

from typing import Literal, TypeAlias, cast

AttributeSuggestionsMode: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeSuggestionsMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttributeSuggestionsMode:
    return cast(AttributeSuggestionsMode, data)
