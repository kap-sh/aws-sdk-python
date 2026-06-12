"""Generated from Smithy shape ``com.amazonaws.snowball#DeviceServiceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

DeviceServiceName: TypeAlias = Literal[
    "NFS_ON_DEVICE_SERVICE",
    "S3_ON_DEVICE_SERVICE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NFS_ON_DEVICE_SERVICE",
        "S3_ON_DEVICE_SERVICE",
    )
)


def serialize_aws_json_1_1(value: DeviceServiceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceServiceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceServiceName value: {data!r}")
    return cast(DeviceServiceName, data)
