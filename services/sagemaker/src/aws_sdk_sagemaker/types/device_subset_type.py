"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceSubsetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

DeviceSubsetType: TypeAlias = Literal[
    "PERCENTAGE",
    "SELECTION",
    "NAMECONTAINS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERCENTAGE",
        "SELECTION",
        "NAMECONTAINS",
    )
)


def serialize_aws_json_1_1(value: DeviceSubsetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceSubsetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceSubsetType value: {data!r}")
    return cast(DeviceSubsetType, data)
