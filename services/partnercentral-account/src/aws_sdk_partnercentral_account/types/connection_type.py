"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionType``."""

from typing import Literal, TypeAlias, cast

ConnectionType: TypeAlias = Literal[
    "OPPORTUNITY_COLLABORATION",
    "SUBSIDIARY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionType:
    return cast(ConnectionType, data)
