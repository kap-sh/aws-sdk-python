"""Generated from Smithy shape ``com.amazonaws.transfer#PreserveFilenameType``."""

from typing import Literal, TypeAlias, cast

PreserveFilenameType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreserveFilenameType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreserveFilenameType:
    return cast(PreserveFilenameType, data)
