"""Generated from Smithy shape ``com.amazonaws.firehose#OrcFormatVersion``."""

from typing import Literal, TypeAlias, cast

OrcFormatVersion: TypeAlias = Literal[
    "V0_11",
    "V0_12",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrcFormatVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrcFormatVersion:
    return cast(OrcFormatVersion, data)
