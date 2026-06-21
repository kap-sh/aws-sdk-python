"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeviceRememberedStatusType``."""

from typing import Literal, TypeAlias, cast

DeviceRememberedStatusType: TypeAlias = Literal[
    "remembered",
    "not_remembered",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceRememberedStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceRememberedStatusType:
    return cast(DeviceRememberedStatusType, data)
