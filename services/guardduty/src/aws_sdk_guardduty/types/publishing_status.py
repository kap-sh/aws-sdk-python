"""Generated from Smithy shape ``com.amazonaws.guardduty#PublishingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

PublishingStatus: TypeAlias = Literal[
    "PENDING_VERIFICATION",
    "PUBLISHING",
    "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_VERIFICATION",
        "PUBLISHING",
        "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY",
        "STOPPED",
    )
)


def serialize_json(value: PublishingStatus) -> str:
    return value


def deserialize_json(data: str) -> PublishingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PublishingStatus value: {data!r}")
    return cast(PublishingStatus, data)
