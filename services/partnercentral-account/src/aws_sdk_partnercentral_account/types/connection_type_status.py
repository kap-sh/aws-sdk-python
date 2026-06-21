"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionTypeStatus``."""

from typing import Literal, TypeAlias, cast

ConnectionTypeStatus: TypeAlias = Literal[
    "ACTIVE",
    "CANCELED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionTypeStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionTypeStatus:
    return cast(ConnectionTypeStatus, data)
