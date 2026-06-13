"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#AutomationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

"""List of status supported by automation jobs"""
AutomationJobStatus: TypeAlias = Literal[
    "Created",
    "InProgress",
    "Success",
    "ServiceError",
    "ClientError",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Created",
        "InProgress",
        "Success",
        "ServiceError",
        "ClientError",
    )
)


def serialize_aws_json_1_1(value: AutomationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomationJobStatus value: {data!r}")
    return cast(AutomationJobStatus, data)
