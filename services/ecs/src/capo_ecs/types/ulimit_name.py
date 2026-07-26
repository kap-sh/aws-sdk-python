"""Generated from Smithy shape ``com.amazonaws.ecs#UlimitName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: UlimitName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UlimitName:
    return cast(UlimitName, data)
