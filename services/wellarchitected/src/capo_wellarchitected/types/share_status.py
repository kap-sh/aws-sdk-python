"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ShareStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the share request.</p>"""
ShareStatus: TypeAlias = Literal[
    "ACCEPTED",
    "REJECTED",
    "PENDING",
    "REVOKED",
    "EXPIRED",
    "ASSOCIATING",
    "ASSOCIATED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareStatus) -> str:
    return value


def deserialize_json(data: str) -> ShareStatus:
    return cast(ShareStatus, data)
