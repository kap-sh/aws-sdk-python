"""Generated from Smithy shape ``com.amazonaws.glue#ResourceShareType``."""

from typing import Literal, TypeAlias, cast

ResourceShareType: TypeAlias = Literal[
    "FOREIGN",
    "ALL",
    "FEDERATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceShareType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceShareType:
    return cast(ResourceShareType, data)
