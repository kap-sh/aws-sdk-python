"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystemName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

OperatingSystemName: TypeAlias = Literal[
    "AMAZON_LINUX_2",
    "UBUNTU_18_04",
    "UBUNTU_20_04",
    "UBUNTU_22_04",
    "UNKNOWN",
    "WINDOWS_10",
    "WINDOWS_11",
    "WINDOWS_7",
    "WINDOWS_SERVER_2016",
    "WINDOWS_SERVER_2019",
    "WINDOWS_SERVER_2022",
    "WINDOWS_SERVER_2025",
    "RHEL_8",
    "ROCKY_8",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AMAZON_LINUX_2",
        "UBUNTU_18_04",
        "UBUNTU_20_04",
        "UBUNTU_22_04",
        "UNKNOWN",
        "WINDOWS_10",
        "WINDOWS_11",
        "WINDOWS_7",
        "WINDOWS_SERVER_2016",
        "WINDOWS_SERVER_2019",
        "WINDOWS_SERVER_2022",
        "WINDOWS_SERVER_2025",
        "RHEL_8",
        "ROCKY_8",
    )
)


def serialize_aws_json_1_1(value: OperatingSystemName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperatingSystemName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperatingSystemName value: {data!r}")
    return cast(OperatingSystemName, data)
