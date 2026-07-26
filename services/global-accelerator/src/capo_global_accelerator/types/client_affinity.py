"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ClientAffinity``."""

from typing import Literal, TypeAlias, cast

ClientAffinity: TypeAlias = Literal[
    "NONE",
    "SOURCE_IP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientAffinity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientAffinity:
    return cast(ClientAffinity, data)
