"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisErrorReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ephemeris_error_reason

EphemerisErrorReasonList: TypeAlias = list[
    "aws_sdk_groundstation.types.ephemeris_error_reason.EphemerisErrorReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisErrorReasonList) -> list:
    import aws_sdk_groundstation.types.ephemeris_error_reason

    out: list = []
    for item in value:
        out.append(
            aws_sdk_groundstation.types.ephemeris_error_reason.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EphemerisErrorReasonList:
    import aws_sdk_groundstation.types.ephemeris_error_reason

    out: EphemerisErrorReasonList = []
    for item in data:
        out.append(
            aws_sdk_groundstation.types.ephemeris_error_reason.deserialize_json(item)
        )
    return out
