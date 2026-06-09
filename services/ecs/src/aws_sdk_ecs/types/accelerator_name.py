"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

AcceleratorName: TypeAlias = Literal[
    "a100",
    "inferentia",
    "k520",
    "k80",
    "m60",
    "radeon-pro-v520",
    "t4",
    "vu9p",
    "v100",
    "a10g",
    "h100",
    "t4g",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "a100",
        "inferentia",
        "k520",
        "k80",
        "m60",
        "radeon-pro-v520",
        "t4",
        "vu9p",
        "v100",
        "a10g",
        "h100",
        "t4g",
    )
)


def serialize_aws_json_1_1(value: AcceleratorName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceleratorName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceleratorName value: {data!r}")
    return cast(AcceleratorName, data)
