"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#PartitionKeyEnforcementLevel``."""

from typing import Literal, TypeAlias, cast

PartitionKeyEnforcementLevel: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartitionKeyEnforcementLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PartitionKeyEnforcementLevel:
    return cast(PartitionKeyEnforcementLevel, data)
