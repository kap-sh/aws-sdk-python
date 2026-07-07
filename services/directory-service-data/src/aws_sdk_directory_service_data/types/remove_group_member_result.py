"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#RemoveGroupMemberResult``."""

from typing_extensions import TypedDict


class RemoveGroupMemberResult(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RemoveGroupMemberResult) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveGroupMemberResult:
    out: RemoveGroupMemberResult = {}  # type: ignore[typeddict-item]
    return out
