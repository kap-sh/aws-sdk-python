"""Generated from Smithy shape ``com.amazonaws.medialive#OfferingDurationUnits``."""

from typing import Literal, TypeAlias, cast

"""Units for duration, e.g. 'MONTHS'"""
OfferingDurationUnits: TypeAlias = Literal["MONTHS",]


# --- restJson1 ser/de ---
def serialize_json(value: OfferingDurationUnits) -> str:
    return value


def deserialize_json(data: str) -> OfferingDurationUnits:
    return cast(OfferingDurationUnits, data)
