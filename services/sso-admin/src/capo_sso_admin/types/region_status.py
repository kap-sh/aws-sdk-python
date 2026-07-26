"""Generated from Smithy shape ``com.amazonaws.ssoadmin#RegionStatus``."""

from typing import Literal, TypeAlias, cast

RegionStatus: TypeAlias = Literal[
    "ACTIVE",
    "ADDING",
    "REMOVING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegionStatus:
    return cast(RegionStatus, data)
