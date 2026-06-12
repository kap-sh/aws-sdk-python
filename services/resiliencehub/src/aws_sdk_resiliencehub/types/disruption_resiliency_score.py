"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DisruptionResiliencyScore``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.disruption_type
    import aws_sdk_resiliencehub.types.double

DisruptionResiliencyScore: TypeAlias = dict[
    "aws_sdk_resiliencehub.types.disruption_type.DisruptionType",
    "aws_sdk_resiliencehub.types.double.Double",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DisruptionResiliencyScore) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_resiliencehub.types.disruption_type

        out[aws_sdk_resiliencehub.types.disruption_type.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> DisruptionResiliencyScore:
    out: DisruptionResiliencyScore = {}
    for key, value in data.items():
        import aws_sdk_resiliencehub.types.disruption_type

        out[aws_sdk_resiliencehub.types.disruption_type.deserialize_json(key)] = value
    return out
