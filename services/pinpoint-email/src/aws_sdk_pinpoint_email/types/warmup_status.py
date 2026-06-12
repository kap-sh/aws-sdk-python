"""Generated from Smithy shape ``com.amazonaws.pinpointemail#WarmupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint_email.errors import DeserializationError

"""<p>The warmup status of a dedicated IP.</p>"""
WarmupStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "DONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "DONE",
    )
)


def serialize_json(value: WarmupStatus) -> str:
    return value


def deserialize_json(data: str) -> WarmupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WarmupStatus value: {data!r}")
    return cast(WarmupStatus, data)
