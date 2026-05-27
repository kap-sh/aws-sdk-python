"""Generated from Smithy shape ``com.amazonaws.eks#labelsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.label_key
    import aws_sdk_eks.types.label_value

labelsMap: TypeAlias = dict[
    "aws_sdk_eks.types.label_key.labelKey", "aws_sdk_eks.types.label_value.labelValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: labelsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> labelsMap:
    out: labelsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
