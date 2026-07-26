"""Generated from Smithy shape ``com.amazonaws.servicequotas#OptInType``."""

from typing import Literal, TypeAlias, cast

OptInType: TypeAlias = Literal[
    "NotifyOnly",
    "NotifyAndAdjust",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptInType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptInType:
    return cast(OptInType, data)
