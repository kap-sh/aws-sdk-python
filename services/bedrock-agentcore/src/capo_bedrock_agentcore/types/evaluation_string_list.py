"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationStringList``."""

from typing import TypeAlias

EvaluationStringList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationStringList:
    return [item for item in data if item is not None]
