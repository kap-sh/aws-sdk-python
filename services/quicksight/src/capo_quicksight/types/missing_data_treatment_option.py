"""Generated from Smithy shape ``com.amazonaws.quicksight#MissingDataTreatmentOption``."""

from typing import Literal, TypeAlias, cast

MissingDataTreatmentOption: TypeAlias = Literal[
    "INTERPOLATE",
    "SHOW_AS_ZERO",
    "SHOW_AS_BLANK",
]


# --- restJson1 ser/de ---
def serialize_json(value: MissingDataTreatmentOption) -> str:
    return value


def deserialize_json(data: str) -> MissingDataTreatmentOption:
    return cast(MissingDataTreatmentOption, data)
