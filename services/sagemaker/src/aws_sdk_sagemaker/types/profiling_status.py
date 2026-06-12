"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProfilingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProfilingStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: ProfilingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProfilingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfilingStatus value: {data!r}")
    return cast(ProfilingStatus, data)
