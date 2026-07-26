"""Generated from Smithy shape ``com.amazonaws.omics#DeleteS3AccessPolicyResponse``."""

from typing_extensions import TypedDict


class DeleteS3AccessPolicyResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteS3AccessPolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteS3AccessPolicyResponse:
    out: DeleteS3AccessPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
