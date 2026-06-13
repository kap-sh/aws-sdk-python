"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#TenancyEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

TenancyEnum: TypeAlias = Literal[
    "default",
    "dedicated",
    "host",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "dedicated",
        "host",
    )
)


def serialize_aws_json_1_0(value: TenancyEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TenancyEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TenancyEnum value: {data!r}")
    return cast(TenancyEnum, data)
