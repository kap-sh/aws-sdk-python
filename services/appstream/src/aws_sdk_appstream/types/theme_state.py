"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeState``."""

from typing import Literal, TypeAlias, cast

ThemeState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThemeState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThemeState:
    return cast(ThemeState, data)
