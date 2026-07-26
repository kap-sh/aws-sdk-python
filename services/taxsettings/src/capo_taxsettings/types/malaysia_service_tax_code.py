"""Generated from Smithy shape ``com.amazonaws.taxsettings#MalaysiaServiceTaxCode``."""

from typing import Literal, TypeAlias, cast

MalaysiaServiceTaxCode: TypeAlias = Literal[
    "Consultancy",
    "Digital Service And Electronic Medium",
    "IT Services",
    "Training Or Coaching",
]


# --- restJson1 ser/de ---
def serialize_json(value: MalaysiaServiceTaxCode) -> str:
    return value


def deserialize_json(data: str) -> MalaysiaServiceTaxCode:
    return cast(MalaysiaServiceTaxCode, data)
