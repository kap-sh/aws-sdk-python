"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OCSFVersion``."""

from typing import Literal, TypeAlias, cast

OCSFVersion: TypeAlias = Literal[
    "V1.1",
    "V1.5",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OCSFVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OCSFVersion:
    return cast(OCSFVersion, data)
