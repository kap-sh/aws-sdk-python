"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ShareInvitationAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

"""<p>Share invitation action taken by contributor.</p>"""
ShareInvitationAction: TypeAlias = Literal[
    "ACCEPT",
    "REJECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCEPT",
        "REJECT",
    )
)


def serialize_json(value: ShareInvitationAction) -> str:
    return value


def deserialize_json(data: str) -> ShareInvitationAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareInvitationAction value: {data!r}")
    return cast(ShareInvitationAction, data)
