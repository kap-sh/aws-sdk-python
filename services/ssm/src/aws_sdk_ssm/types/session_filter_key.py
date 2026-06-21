"""Generated from Smithy shape ``com.amazonaws.ssm#SessionFilterKey``."""

from typing import Literal, TypeAlias, cast

SessionFilterKey: TypeAlias = Literal[
    "InvokedAfter",
    "InvokedBefore",
    "Target",
    "Owner",
    "Status",
    "SessionId",
    "AccessType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionFilterKey:
    return cast(SessionFilterKey, data)
