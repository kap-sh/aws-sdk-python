"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceVersion``."""

from typing import Literal, TypeAlias, cast

ConfluenceVersion: TypeAlias = Literal[
    "CLOUD",
    "SERVER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceVersion:
    return cast(ConfluenceVersion, data)
