"""Generated from Smithy shape ``com.amazonaws.mpa#ApproverLastActivity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

ApproverLastActivity: TypeAlias = Literal[
    "VOTED",
    "BASELINED",
    "RESPONDED_TO_INVITATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VOTED",
        "BASELINED",
        "RESPONDED_TO_INVITATION",
    )
)


def serialize_json(value: ApproverLastActivity) -> str:
    return value


def deserialize_json(data: str) -> ApproverLastActivity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApproverLastActivity value: {data!r}")
    return cast(ApproverLastActivity, data)
