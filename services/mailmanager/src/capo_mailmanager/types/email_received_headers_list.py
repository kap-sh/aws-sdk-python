"""Generated from Smithy shape ``com.amazonaws.mailmanager#EmailReceivedHeadersList``."""

from typing import TypeAlias

EmailReceivedHeadersList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EmailReceivedHeadersList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> EmailReceivedHeadersList:
    return list(data)
