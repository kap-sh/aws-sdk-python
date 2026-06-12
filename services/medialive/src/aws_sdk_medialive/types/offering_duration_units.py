"""Generated from Smithy shape ``com.amazonaws.medialive#OfferingDurationUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Units for duration, e.g. 'MONTHS'"""
OfferingDurationUnits: TypeAlias = Literal["MONTHS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MONTHS",))


def serialize_json(value: OfferingDurationUnits) -> str:
    return value


def deserialize_json(data: str) -> OfferingDurationUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferingDurationUnits value: {data!r}")
    return cast(OfferingDurationUnits, data)
