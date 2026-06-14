"""Generated from Smithy shape ``com.amazonaws.workspaces#UserSettingActionEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

UserSettingActionEnum: TypeAlias = Literal[
    "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
    "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
    "PRINTING_TO_LOCAL_DEVICE",
    "SMART_CARD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
        "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
        "PRINTING_TO_LOCAL_DEVICE",
        "SMART_CARD",
    )
)


def serialize_aws_json_1_1(value: UserSettingActionEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserSettingActionEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserSettingActionEnum value: {data!r}")
    return cast(UserSettingActionEnum, data)
