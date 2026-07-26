"""Generated from Smithy shape ``com.amazonaws.odb#DiskRedundancy``."""

from typing import Literal, TypeAlias, cast

DiskRedundancy: TypeAlias = Literal[
    "HIGH",
    "NORMAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DiskRedundancy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DiskRedundancy:
    return cast(DiskRedundancy, data)
