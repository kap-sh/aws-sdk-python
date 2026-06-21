"""Generated from Smithy shape ``com.amazonaws.codecommit#OverrideStatus``."""

from typing import Literal, TypeAlias, cast

OverrideStatus: TypeAlias = Literal[
    "OVERRIDE",
    "REVOKE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverrideStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OverrideStatus:
    return cast(OverrideStatus, data)
