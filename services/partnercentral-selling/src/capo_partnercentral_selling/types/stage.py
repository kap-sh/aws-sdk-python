"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Stage``."""

from typing import Literal, TypeAlias, cast

Stage: TypeAlias = Literal[
    "Prospect",
    "Qualified",
    "Technical Validation",
    "Business Validation",
    "Committed",
    "Launched",
    "Closed Lost",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Stage) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Stage:
    return cast(Stage, data)
