"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AcceleratorStatus``."""

from typing import Literal, TypeAlias, cast

AcceleratorStatus: TypeAlias = Literal[
    "DEPLOYED",
    "IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceleratorStatus:
    return cast(AcceleratorStatus, data)
