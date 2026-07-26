"""Generated from Smithy shape ``com.amazonaws.taxsettings#GetTaxExemptionTypesRequest``."""

from typing_extensions import TypedDict


class GetTaxExemptionTypesRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetTaxExemptionTypesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTaxExemptionTypesRequest:
    out: GetTaxExemptionTypesRequest = {}  # type: ignore[typeddict-item]
    return out
