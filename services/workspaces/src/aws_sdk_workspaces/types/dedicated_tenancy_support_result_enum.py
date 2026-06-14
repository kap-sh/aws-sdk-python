"""Generated from Smithy shape ``com.amazonaws.workspaces#DedicatedTenancySupportResultEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

DedicatedTenancySupportResultEnum: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: DedicatedTenancySupportResultEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DedicatedTenancySupportResultEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DedicatedTenancySupportResultEnum value: {data!r}"
        )
    return cast(DedicatedTenancySupportResultEnum, data)
