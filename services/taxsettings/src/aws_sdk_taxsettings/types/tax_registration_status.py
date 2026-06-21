"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationStatus``."""

from typing import Literal, TypeAlias, cast

TaxRegistrationStatus: TypeAlias = Literal[
    "Verified",
    "Pending",
    "Deleted",
    "Rejected",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationStatus) -> str:
    return value


def deserialize_json(data: str) -> TaxRegistrationStatus:
    return cast(TaxRegistrationStatus, data)
