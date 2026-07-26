"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfModelScores``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.model_scores

ListOfModelScores: TypeAlias = list["capo_frauddetector.types.model_scores.ModelScores"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfModelScores) -> list:
    import capo_frauddetector.types.model_scores

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.model_scores.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfModelScores:
    import capo_frauddetector.types.model_scores

    out: ListOfModelScores = []
    for item in data:
        out.append(capo_frauddetector.types.model_scores.deserialize_aws_json_1_1(item))
    return out
