"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#PostContactSummaryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect_contact_lens.errors import DeserializationError

PostContactSummaryStatus: TypeAlias = Literal[
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: PostContactSummaryStatus) -> str:
    return value


def deserialize_json(data: str) -> PostContactSummaryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PostContactSummaryStatus value: {data!r}")
    return cast(PostContactSummaryStatus, data)
