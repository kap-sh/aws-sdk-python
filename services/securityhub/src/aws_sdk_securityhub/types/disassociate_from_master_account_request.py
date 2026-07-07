"""Generated from Smithy shape ``com.amazonaws.securityhub#DisassociateFromMasterAccountRequest``."""

from typing_extensions import TypedDict


class DisassociateFromMasterAccountRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateFromMasterAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateFromMasterAccountRequest:
    out: DisassociateFromMasterAccountRequest = {}  # type: ignore[typeddict-item]
    return out
