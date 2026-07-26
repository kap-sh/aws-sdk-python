"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutTaxInheritanceResponse``."""

from typing_extensions import TypedDict


class PutTaxInheritanceResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutTaxInheritanceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutTaxInheritanceResponse:
    out: PutTaxInheritanceResponse = {}  # type: ignore[typeddict-item]
    return out
