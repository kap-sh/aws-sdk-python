"""Generated from Smithy shape ``com.amazonaws.appstream#Action``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

Action: TypeAlias = Literal[
    "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
    "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
    "FILE_UPLOAD",
    "FILE_DOWNLOAD",
    "PRINTING_TO_LOCAL_DEVICE",
    "DOMAIN_PASSWORD_SIGNIN",
    "DOMAIN_SMART_CARD_SIGNIN",
    "AUTO_TIME_ZONE_REDIRECTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
        "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
        "FILE_UPLOAD",
        "FILE_DOWNLOAD",
        "PRINTING_TO_LOCAL_DEVICE",
        "DOMAIN_PASSWORD_SIGNIN",
        "DOMAIN_SMART_CARD_SIGNIN",
        "AUTO_TIME_ZONE_REDIRECTION",
    )
)


def serialize_aws_json_1_1(value: Action) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Action:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Action value: {data!r}")
    return cast(Action, data)
