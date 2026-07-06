"""Generated from Smithy shape ``com.amazonaws.s3files#PutFileSystemPolicyResponse``."""

from typing_extensions import TypedDict


class PutFileSystemPolicyResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutFileSystemPolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutFileSystemPolicyResponse:
    out: PutFileSystemPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
