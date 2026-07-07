"""Generated from Smithy shape ``com.amazonaws.taxsettings#PhilippinesAdditionalInfo``."""

from typing_extensions import NotRequired, TypedDict


class PhilippinesAdditionalInfo(TypedDict, closed=True):
    is_vat_registered: NotRequired["bool"]
    """<p>Indicates whether the account is VAT-registered with the Philippines Bureau of Internal Revenue (BIR).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhilippinesAdditionalInfo) -> dict:
    out: dict = {}
    if "is_vat_registered" in value:
        out["isVatRegistered"] = value["is_vat_registered"]
    return out


def deserialize_json(data: dict) -> PhilippinesAdditionalInfo:
    out: PhilippinesAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "isVatRegistered" in data:
        out["is_vat_registered"] = data["isVatRegistered"]
    return out
