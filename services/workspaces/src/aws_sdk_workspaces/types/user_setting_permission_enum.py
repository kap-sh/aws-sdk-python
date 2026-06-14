"""Generated from Smithy shape ``com.amazonaws.workspaces#UserSettingPermissionEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

UserSettingPermissionEnum: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: UserSettingPermissionEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserSettingPermissionEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserSettingPermissionEnum value: {data!r}")
    return cast(UserSettingPermissionEnum, data)
