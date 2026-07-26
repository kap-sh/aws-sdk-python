"""Generated from Smithy shape ``com.amazonaws.lightsail#BPAStatusMessage``."""

from typing import Literal, TypeAlias, cast

BPAStatusMessage: TypeAlias = Literal[
    "DEFAULTED_FOR_SLR_MISSING",
    "SYNC_ON_HOLD",
    "DEFAULTED_FOR_SLR_MISSING_ON_HOLD",
    "Unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BPAStatusMessage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BPAStatusMessage:
    return cast(BPAStatusMessage, data)
