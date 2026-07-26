"""Generated from Smithy shape ``com.amazonaws.kendra#UserContextPolicy``."""

from typing import Literal, TypeAlias, cast

UserContextPolicy: TypeAlias = Literal[
    "ATTRIBUTE_FILTER",
    "USER_TOKEN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserContextPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserContextPolicy:
    return cast(UserContextPolicy, data)
