"""Generated from Smithy shape ``com.amazonaws.firehose#SSLMode``."""

from typing import Literal, TypeAlias, cast

SSLMode: TypeAlias = Literal[
    "Disabled",
    "Enabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SSLMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SSLMode:
    return cast(SSLMode, data)
