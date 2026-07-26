"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ShareInvitationAction``."""

from typing import Literal, TypeAlias, cast

"""<p>Share invitation action taken by contributor.</p>"""
ShareInvitationAction: TypeAlias = Literal[
    "ACCEPT",
    "REJECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareInvitationAction) -> str:
    return value


def deserialize_json(data: str) -> ShareInvitationAction:
    return cast(ShareInvitationAction, data)
