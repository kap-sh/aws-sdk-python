"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceFormFactor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

DeviceFormFactor: TypeAlias = Literal[
    "PHONE",
    "TABLET",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PHONE",
        "TABLET",
    )
)


def serialize_aws_json_1_1(value: DeviceFormFactor) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceFormFactor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceFormFactor value: {data!r}")
    return cast(DeviceFormFactor, data)
