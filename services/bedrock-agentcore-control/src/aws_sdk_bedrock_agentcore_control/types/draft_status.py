"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DraftStatus``."""

from typing import Literal, TypeAlias, cast

"""<p> Publish synchronization state of the DRAFT working copy. </p>"""
DraftStatus: TypeAlias = Literal[
    "MODIFIED",
    "UNMODIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DraftStatus) -> str:
    return value


def deserialize_json(data: str) -> DraftStatus:
    return cast(DraftStatus, data)
