"""Generated from Smithy shape ``com.amazonaws.ssm#OperatingSystem``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

OperatingSystem: TypeAlias = Literal[
    "WINDOWS",
    "AMAZON_LINUX",
    "AMAZON_LINUX_2",
    "AMAZON_LINUX_2022",
    "UBUNTU",
    "REDHAT_ENTERPRISE_LINUX",
    "SUSE",
    "CENTOS",
    "ORACLE_LINUX",
    "DEBIAN",
    "MACOS",
    "RASPBIAN",
    "ROCKY_LINUX",
    "ALMA_LINUX",
    "AMAZON_LINUX_2023",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS",
        "AMAZON_LINUX",
        "AMAZON_LINUX_2",
        "AMAZON_LINUX_2022",
        "UBUNTU",
        "REDHAT_ENTERPRISE_LINUX",
        "SUSE",
        "CENTOS",
        "ORACLE_LINUX",
        "DEBIAN",
        "MACOS",
        "RASPBIAN",
        "ROCKY_LINUX",
        "ALMA_LINUX",
        "AMAZON_LINUX_2023",
    )
)


def serialize_aws_json_1_1(value: OperatingSystem) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperatingSystem:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperatingSystem value: {data!r}")
    return cast(OperatingSystem, data)
