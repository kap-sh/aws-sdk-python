"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RefreshScheduleStatus``."""

from typing import Literal, TypeAlias, cast

RefreshScheduleStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshScheduleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RefreshScheduleStatus:
    return cast(RefreshScheduleStatus, data)
