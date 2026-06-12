"""Generated from Smithy shape ``com.amazonaws.eventbridge#TransformerPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.input_transformer_path_key
    import aws_sdk_eventbridge.types.target_input_path

TransformerPaths: TypeAlias = dict[
    "aws_sdk_eventbridge.types.input_transformer_path_key.InputTransformerPathKey",
    "aws_sdk_eventbridge.types.target_input_path.TargetInputPath",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TransformerPaths) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformerPaths:
    out: TransformerPaths = {}
    for key, value in data.items():
        out[key] = value
    return out
