"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListDeviceFleetsSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ListDeviceFleetsSortBy: TypeAlias = Literal[
    "NAME",
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "CREATION_TIME",
        "LAST_MODIFIED_TIME",
    )
)


def serialize_aws_json_1_1(value: ListDeviceFleetsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListDeviceFleetsSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListDeviceFleetsSortBy value: {data!r}")
    return cast(ListDeviceFleetsSortBy, data)
