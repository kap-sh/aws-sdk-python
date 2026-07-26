"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContinuousBackupsStatus``."""

from typing import Literal, TypeAlias, cast

ContinuousBackupsStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContinuousBackupsStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContinuousBackupsStatus:
    return cast(ContinuousBackupsStatus, data)
