"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceFormFactor``."""

from typing import Literal, TypeAlias, cast

DeviceFormFactor: TypeAlias = Literal[
    "PHONE",
    "TABLET",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceFormFactor) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceFormFactor:
    return cast(DeviceFormFactor, data)
