"""Generated from Smithy shape ``com.amazonaws.taxsettings#Industries``."""

from typing import Literal, TypeAlias, cast

Industries: TypeAlias = Literal[
    "CirculatingOrg",
    "ProfessionalOrg",
    "Banks",
    "Insurance",
    "PensionAndBenefitFunds",
    "DevelopmentAgencies",
]


# --- restJson1 ser/de ---
def serialize_json(value: Industries) -> str:
    return value


def deserialize_json(data: str) -> Industries:
    return cast(Industries, data)
