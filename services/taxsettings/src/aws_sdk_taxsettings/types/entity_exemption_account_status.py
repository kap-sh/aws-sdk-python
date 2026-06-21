"""Generated from Smithy shape ``com.amazonaws.taxsettings#EntityExemptionAccountStatus``."""

from typing import Literal, TypeAlias, cast

EntityExemptionAccountStatus: TypeAlias = Literal[
    "None",
    "Valid",
    "Expired",
    "Pending",
]


# --- restJson1 ser/de ---
def serialize_json(value: EntityExemptionAccountStatus) -> str:
    return value


def deserialize_json(data: str) -> EntityExemptionAccountStatus:
    return cast(EntityExemptionAccountStatus, data)
