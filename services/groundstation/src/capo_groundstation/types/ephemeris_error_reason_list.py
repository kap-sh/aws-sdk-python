"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisErrorReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.ephemeris_error_reason

EphemerisErrorReasonList: TypeAlias = list[
    "capo_groundstation.types.ephemeris_error_reason.EphemerisErrorReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisErrorReasonList) -> list:
    import capo_groundstation.types.ephemeris_error_reason

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.ephemeris_error_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> EphemerisErrorReasonList:
    import capo_groundstation.types.ephemeris_error_reason

    out: EphemerisErrorReasonList = []
    for item in data:
        out.append(
            capo_groundstation.types.ephemeris_error_reason.deserialize_json(item)
        )
    return out
