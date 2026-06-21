"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#AutomationJobStatus``."""

from typing import Literal, TypeAlias, cast

"""List of status supported by automation jobs"""
AutomationJobStatus: TypeAlias = Literal[
    "Created",
    "InProgress",
    "Success",
    "ServiceError",
    "ClientError",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationJobStatus:
    return cast(AutomationJobStatus, data)
