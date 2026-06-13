"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CpuCreditsEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

CpuCreditsEnum: TypeAlias = Literal[
    "standard",
    "unlimited",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "unlimited",
    )
)


def serialize_aws_json_1_0(value: CpuCreditsEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CpuCreditsEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CpuCreditsEnum value: {data!r}")
    return cast(CpuCreditsEnum, data)
