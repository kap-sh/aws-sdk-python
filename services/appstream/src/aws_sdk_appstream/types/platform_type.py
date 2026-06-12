"""Generated from Smithy shape ``com.amazonaws.appstream#PlatformType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

PlatformType: TypeAlias = Literal[
    "WINDOWS",
    "WINDOWS_SERVER_2016",
    "WINDOWS_SERVER_2019",
    "WINDOWS_SERVER_2022",
    "WINDOWS_SERVER_2025",
    "AMAZON_LINUX2",
    "RHEL8",
    "ROCKY_LINUX8",
    "UBUNTU_PRO_2404",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS",
        "WINDOWS_SERVER_2016",
        "WINDOWS_SERVER_2019",
        "WINDOWS_SERVER_2022",
        "WINDOWS_SERVER_2025",
        "AMAZON_LINUX2",
        "RHEL8",
        "ROCKY_LINUX8",
        "UBUNTU_PRO_2404",
    )
)


def serialize_aws_json_1_1(value: PlatformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlatformType value: {data!r}")
    return cast(PlatformType, data)
