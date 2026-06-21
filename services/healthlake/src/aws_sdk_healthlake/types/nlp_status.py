"""Generated from Smithy shape ``com.amazonaws.healthlake#NlpStatus``."""

from typing import Literal, TypeAlias, cast

NlpStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLING",
    "DISABLING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NlpStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NlpStatus:
    return cast(NlpStatus, data)
