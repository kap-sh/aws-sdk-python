"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.landing_zone_operation_type

LandingZoneOperationTypes: TypeAlias = list[
    "aws_sdk_controltower.types.landing_zone_operation_type.LandingZoneOperationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneOperationTypes) -> list:
    import aws_sdk_controltower.types.landing_zone_operation_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_controltower.types.landing_zone_operation_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LandingZoneOperationTypes:
    import aws_sdk_controltower.types.landing_zone_operation_type

    out: LandingZoneOperationTypes = []
    for item in data:
        out.append(
            aws_sdk_controltower.types.landing_zone_operation_type.deserialize_json(
                item
            )
        )
    return out
