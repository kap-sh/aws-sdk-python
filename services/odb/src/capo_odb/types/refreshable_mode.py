"""Generated from Smithy shape ``com.amazonaws.odb#RefreshableMode``."""

from typing import Literal, TypeAlias, cast

RefreshableMode: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RefreshableMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RefreshableMode:
    return cast(RefreshableMode, data)
