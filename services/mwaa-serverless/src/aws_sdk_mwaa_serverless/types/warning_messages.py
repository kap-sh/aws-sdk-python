"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WarningMessages``."""

from typing import TypeAlias

WarningMessages: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WarningMessages) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> WarningMessages:
    return list(data)
