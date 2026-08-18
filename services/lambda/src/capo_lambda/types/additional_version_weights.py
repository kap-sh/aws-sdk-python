"""Generated from Smithy shape ``com.amazonaws.lambda#AdditionalVersionWeights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.additional_version
    import capo_lambda.types.weight

AdditionalVersionWeights: TypeAlias = dict[
    "capo_lambda.types.additional_version.AdditionalVersion",
    "capo_lambda.types.weight.Weight",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdditionalVersionWeights) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = (
            "NaN"
            if value != value
            else "Infinity"
            if value == float("inf")
            else "-Infinity"
            if value == float("-inf")
            else value
        )
    return out


def deserialize_json(data: dict) -> AdditionalVersionWeights:
    out: AdditionalVersionWeights = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = float(value)
    return out
