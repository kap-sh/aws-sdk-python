"""Generated from Smithy shape ``com.amazonaws.taxsettings#IndonesiaTaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

IndonesiaTaxRegistrationNumberType: TypeAlias = Literal[
    "NIK",
    "PassportNumber",
    "NPWP",
    "NITKU",
]


# --- restJson1 ser/de ---
def serialize_json(value: IndonesiaTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> IndonesiaTaxRegistrationNumberType:
    return cast(IndonesiaTaxRegistrationNumberType, data)
