"""Generated from Smithy shape ``com.amazonaws.bedrock#ProvisionedModelStatus``."""

from typing import Literal, TypeAlias, cast

ProvisionedModelStatus: TypeAlias = Literal[
    "Creating",
    "InService",
    "Updating",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ProvisionedModelStatus:
    return cast(ProvisionedModelStatus, data)
