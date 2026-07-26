"""Generated from Smithy shape ``com.amazonaws.eventbridge#AssignPublicIp``."""

from typing import Literal, TypeAlias, cast

AssignPublicIp: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssignPublicIp) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssignPublicIp:
    return cast(AssignPublicIp, data)
