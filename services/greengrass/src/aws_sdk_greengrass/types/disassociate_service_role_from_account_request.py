"""Generated from Smithy shape ``com.amazonaws.greengrass#DisassociateServiceRoleFromAccountRequest``."""

from typing_extensions import TypedDict


class DisassociateServiceRoleFromAccountRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateServiceRoleFromAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateServiceRoleFromAccountRequest:
    out: DisassociateServiceRoleFromAccountRequest = {}  # type: ignore[typeddict-item]
    return out
