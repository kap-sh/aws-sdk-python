"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListDeviceFleetsSortBy``."""

from typing import Literal, TypeAlias, cast

ListDeviceFleetsSortBy: TypeAlias = Literal[
    "NAME",
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeviceFleetsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListDeviceFleetsSortBy:
    return cast(ListDeviceFleetsSortBy, data)
