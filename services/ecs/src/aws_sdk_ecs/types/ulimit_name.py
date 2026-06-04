"""Generated from Smithy shape ``com.amazonaws.ecs#UlimitName``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

UlimitName: TypeAlias = Literal[
    "core",
    "cpu",
    "data",
    "fsize",
    "locks",
    "memlock",
    "msgqueue",
    "nice",
    "nofile",
    "nproc",
    "rss",
    "rtprio",
    "rttime",
    "sigpending",
    "stack",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "core",
        "cpu",
        "data",
        "fsize",
        "locks",
        "memlock",
        "msgqueue",
        "nice",
        "nofile",
        "nproc",
        "rss",
        "rtprio",
        "rttime",
        "sigpending",
        "stack",
    )
)


def serialize_aws_json_1_1(value: UlimitName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UlimitName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UlimitName value: {data!r}")
    return cast(UlimitName, data)
