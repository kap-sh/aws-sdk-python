"""Generated from Smithy shape ``com.amazonaws.route53resolver#Action``."""

from typing import Literal, TypeAlias, cast

Action: TypeAlias = Literal[
    "ALLOW",
    "BLOCK",
    "ALERT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Action) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Action:
    return cast(Action, data)
