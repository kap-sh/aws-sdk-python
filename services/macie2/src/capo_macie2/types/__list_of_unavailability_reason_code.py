"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfUnavailabilityReasonCode``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.unavailability_reason_code

__listOfUnavailabilityReasonCode: TypeAlias = list[
    "capo_macie2.types.unavailability_reason_code.UnavailabilityReasonCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUnavailabilityReasonCode) -> list:
    import capo_macie2.types.unavailability_reason_code

    out: list = []
    for item in value:
        out.append(capo_macie2.types.unavailability_reason_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUnavailabilityReasonCode:
    import capo_macie2.types.unavailability_reason_code

    out: __listOfUnavailabilityReasonCode = []
    for item in data:
        out.append(capo_macie2.types.unavailability_reason_code.deserialize_json(item))
    return out
