"""Generated from Smithy shape ``com.amazonaws.odb#RefreshableStatus``."""

from typing import Literal, TypeAlias, cast

RefreshableStatus: TypeAlias = Literal[
    "REFRESHING",
    "NOT_REFRESHING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RefreshableStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RefreshableStatus:
    return cast(RefreshableStatus, data)
