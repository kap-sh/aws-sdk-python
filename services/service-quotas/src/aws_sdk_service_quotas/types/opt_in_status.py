"""Generated from Smithy shape ``com.amazonaws.servicequotas#OptInStatus``."""

from typing import Literal, TypeAlias, cast

OptInStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptInStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptInStatus:
    return cast(OptInStatus, data)
