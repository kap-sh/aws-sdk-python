"""Generated from Smithy shape ``com.amazonaws.ecr#Annotations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.string

Annotations: TypeAlias = dict[
    "capo_ecr.types.string.String", "capo_ecr.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Annotations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Annotations:
    out: Annotations = {}
    for key, value in data.items():
        out[key] = value
    return out
