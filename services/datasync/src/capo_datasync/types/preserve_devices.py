"""Generated from Smithy shape ``com.amazonaws.datasync#PreserveDevices``."""

from typing import Literal, TypeAlias, cast

PreserveDevices: TypeAlias = Literal[
    "NONE",
    "PRESERVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreserveDevices) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreserveDevices:
    return cast(PreserveDevices, data)
