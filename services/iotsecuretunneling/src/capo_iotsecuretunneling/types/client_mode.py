"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#ClientMode``."""

from typing import Literal, TypeAlias, cast

ClientMode: TypeAlias = Literal[
    "SOURCE",
    "DESTINATION",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientMode:
    return cast(ClientMode, data)
