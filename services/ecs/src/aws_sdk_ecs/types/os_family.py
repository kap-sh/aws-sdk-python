"""Generated from Smithy shape ``com.amazonaws.ecs#OSFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

OSFamily: TypeAlias = Literal[
    "WINDOWS_SERVER_2019_FULL",
    "WINDOWS_SERVER_2019_CORE",
    "WINDOWS_SERVER_2016_FULL",
    "WINDOWS_SERVER_2004_CORE",
    "WINDOWS_SERVER_2022_CORE",
    "WINDOWS_SERVER_2022_FULL",
    "WINDOWS_SERVER_2025_CORE",
    "WINDOWS_SERVER_2025_FULL",
    "WINDOWS_SERVER_20H2_CORE",
    "LINUX",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS_SERVER_2019_FULL",
        "WINDOWS_SERVER_2019_CORE",
        "WINDOWS_SERVER_2016_FULL",
        "WINDOWS_SERVER_2004_CORE",
        "WINDOWS_SERVER_2022_CORE",
        "WINDOWS_SERVER_2022_FULL",
        "WINDOWS_SERVER_2025_CORE",
        "WINDOWS_SERVER_2025_FULL",
        "WINDOWS_SERVER_20H2_CORE",
        "LINUX",
    )
)


def serialize_aws_json_1_1(value: OSFamily) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OSFamily:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OSFamily value: {data!r}")
    return cast(OSFamily, data)
