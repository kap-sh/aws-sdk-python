"""Generated from Smithy shape ``com.amazonaws.glue#RegistryStatus``."""

from typing import Literal, TypeAlias, cast

RegistryStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegistryStatus:
    return cast(RegistryStatus, data)
