"""Generated from Smithy shape ``com.amazonaws.eks#DisassociateAccessPolicyResponse``."""

from typing_extensions import TypedDict


class DisassociateAccessPolicyResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAccessPolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateAccessPolicyResponse:
    out: DisassociateAccessPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
