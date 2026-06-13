"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceConfigurationTenancyEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

InstanceConfigurationTenancyEnum: TypeAlias = Literal[
    "SHARED",
    "DEDICATED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHARED",
        "DEDICATED",
    )
)


def serialize_aws_json_1_0(value: InstanceConfigurationTenancyEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceConfigurationTenancyEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceConfigurationTenancyEnum value: {data!r}"
        )
    return cast(InstanceConfigurationTenancyEnum, data)
