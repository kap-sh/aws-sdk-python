"""Generated from Smithy shape ``com.amazonaws.lightsail#AppCategory``."""

from typing import Literal, TypeAlias, cast

AppCategory: TypeAlias = Literal["LfR",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppCategory:
    return cast(AppCategory, data)
