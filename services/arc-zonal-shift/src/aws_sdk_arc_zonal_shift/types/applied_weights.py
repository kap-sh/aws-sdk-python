"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AppliedWeights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.availability_zone
    import aws_sdk_arc_zonal_shift.types.weight

AppliedWeights: TypeAlias = dict[
    "aws_sdk_arc_zonal_shift.types.availability_zone.AvailabilityZone",
    "aws_sdk_arc_zonal_shift.types.weight.Weight",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AppliedWeights) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AppliedWeights:
    out: AppliedWeights = {}
    for key, value in data.items():
        out[key] = value
    return out
