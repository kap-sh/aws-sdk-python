"""Generated from Smithy shape ``com.amazonaws.kendra#SlackEntity``."""

from typing import Literal, TypeAlias, cast

SlackEntity: TypeAlias = Literal[
    "PUBLIC_CHANNEL",
    "PRIVATE_CHANNEL",
    "GROUP_MESSAGE",
    "DIRECT_MESSAGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SlackEntity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SlackEntity:
    return cast(SlackEntity, data)
