"""Generated from Smithy shape ``com.amazonaws.machinelearning#ScoreValuePerLabelMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_machine_learning.types.label
    import capo_machine_learning.types.score_value

ScoreValuePerLabelMap: TypeAlias = dict[
    "capo_machine_learning.types.label.Label",
    "capo_machine_learning.types.score_value.ScoreValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ScoreValuePerLabelMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ScoreValuePerLabelMap:
    out: ScoreValuePerLabelMap = {}
    for key, value in data.items():
        out[key] = value
    return out
