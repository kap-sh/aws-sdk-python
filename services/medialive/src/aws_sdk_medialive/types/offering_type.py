"""Generated from Smithy shape ``com.amazonaws.medialive#OfferingType``."""

from typing import Literal, TypeAlias, cast

"""Offering type, e.g. 'NO_UPFRONT'"""
OfferingType: TypeAlias = Literal["NO_UPFRONT",]


# --- restJson1 ser/de ---
def serialize_json(value: OfferingType) -> str:
    return value


def deserialize_json(data: str) -> OfferingType:
    return cast(OfferingType, data)
