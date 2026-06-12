"""Generated from Smithy shape ``com.amazonaws.sesv2#WarmupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The warmup status of a dedicated IP.</p>"""
WarmupStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "DONE",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "DONE",
        "NOT_APPLICABLE",
    )
)


def serialize_json(value: WarmupStatus) -> str:
    return value


def deserialize_json(data: str) -> WarmupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WarmupStatus value: {data!r}")
    return cast(WarmupStatus, data)
