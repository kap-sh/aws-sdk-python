"""Generated from Smithy shape ``com.amazonaws.kendra#KeyLocation``."""

from typing import Literal, TypeAlias, cast

KeyLocation: TypeAlias = Literal[
    "URL",
    "SECRET_MANAGER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyLocation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyLocation:
    return cast(KeyLocation, data)
