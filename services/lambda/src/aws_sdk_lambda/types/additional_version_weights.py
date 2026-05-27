"""Generated from Smithy shape ``com.amazonaws.lambda#AdditionalVersionWeights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.additional_version
    import aws_sdk_lambda.types.weight

AdditionalVersionWeights: TypeAlias = dict[
    "aws_sdk_lambda.types.additional_version.AdditionalVersion",
    "aws_sdk_lambda.types.weight.Weight",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdditionalVersionWeights) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AdditionalVersionWeights:
    out: AdditionalVersionWeights = {}
    for key, value in data.items():
        out[key] = value
    return out
