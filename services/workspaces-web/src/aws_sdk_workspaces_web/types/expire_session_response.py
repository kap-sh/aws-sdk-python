"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ExpireSessionResponse``."""

from typing_extensions import TypedDict


class ExpireSessionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ExpireSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExpireSessionResponse:
    out: ExpireSessionResponse = {}  # type: ignore[typeddict-item]
    return out
