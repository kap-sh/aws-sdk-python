"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationVisibility``."""

from typing import Literal, TypeAlias, cast

ApplicationVisibility: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationVisibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationVisibility:
    return cast(ApplicationVisibility, data)
