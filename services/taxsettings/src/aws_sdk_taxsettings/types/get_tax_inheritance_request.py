"""Generated from Smithy shape ``com.amazonaws.taxsettings#GetTaxInheritanceRequest``."""

from typing_extensions import TypedDict


class GetTaxInheritanceRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetTaxInheritanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTaxInheritanceRequest:
    out: GetTaxInheritanceRequest = {}  # type: ignore[typeddict-item]
    return out
