"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfUnavailabilityReasonCode``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.unavailability_reason_code

__listOfUnavailabilityReasonCode: TypeAlias = list[
    "aws_sdk_macie2.types.unavailability_reason_code.UnavailabilityReasonCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUnavailabilityReasonCode) -> list:
    import aws_sdk_macie2.types.unavailability_reason_code

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.unavailability_reason_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUnavailabilityReasonCode:
    import aws_sdk_macie2.types.unavailability_reason_code

    out: __listOfUnavailabilityReasonCode = []
    for item in data:
        out.append(
            aws_sdk_macie2.types.unavailability_reason_code.deserialize_json(item)
        )
    return out
