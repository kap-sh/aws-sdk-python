"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ScoringComponentResiliencyScores``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.resiliency_score_type
    import aws_sdk_resiliencehub.types.scoring_component_resiliency_score

ScoringComponentResiliencyScores: TypeAlias = dict[
    "aws_sdk_resiliencehub.types.resiliency_score_type.ResiliencyScoreType",
    "aws_sdk_resiliencehub.types.scoring_component_resiliency_score.ScoringComponentResiliencyScore",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ScoringComponentResiliencyScores) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_resiliencehub.types.resiliency_score_type
        import aws_sdk_resiliencehub.types.scoring_component_resiliency_score

        out[aws_sdk_resiliencehub.types.resiliency_score_type.serialize_json(key)] = (
            aws_sdk_resiliencehub.types.scoring_component_resiliency_score.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ScoringComponentResiliencyScores:
    out: ScoringComponentResiliencyScores = {}
    for key, value in data.items():
        import aws_sdk_resiliencehub.types.resiliency_score_type
        import aws_sdk_resiliencehub.types.scoring_component_resiliency_score

        out[aws_sdk_resiliencehub.types.resiliency_score_type.deserialize_json(key)] = (
            aws_sdk_resiliencehub.types.scoring_component_resiliency_score.deserialize_json(
                value
            )
        )
    return out
