"""Generated from Smithy shape ``com.amazonaws.workspaces#ReconnectEnum``."""

from typing import Literal, TypeAlias, cast

ReconnectEnum: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReconnectEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReconnectEnum:
    return cast(ReconnectEnum, data)
