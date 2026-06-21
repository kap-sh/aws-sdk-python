"""Generated from Smithy shape ``com.amazonaws.storagegateway#CaseSensitivity``."""

from typing import Literal, TypeAlias, cast

CaseSensitivity: TypeAlias = Literal[
    "ClientSpecified",
    "CaseSensitive",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaseSensitivity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CaseSensitivity:
    return cast(CaseSensitivity, data)
