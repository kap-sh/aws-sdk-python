"""Generated from Smithy shape ``com.amazonaws.transfer#PreserveContentType``."""

from typing import Literal, TypeAlias, cast

PreserveContentType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreserveContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreserveContentType:
    return cast(PreserveContentType, data)
