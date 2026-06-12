"""Generated from Smithy shape ``com.amazonaws.personalize#RankingInfluence``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.ranking_influence_type
    import aws_sdk_personalize.types.ranking_influence_weight

RankingInfluence: TypeAlias = dict[
    "aws_sdk_personalize.types.ranking_influence_type.RankingInfluenceType",
    "aws_sdk_personalize.types.ranking_influence_weight.RankingInfluenceWeight",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RankingInfluence) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_personalize.types.ranking_influence_type

        out[
            aws_sdk_personalize.types.ranking_influence_type.serialize_aws_json_1_1(key)
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> RankingInfluence:
    out: RankingInfluence = {}
    for key, value in data.items():
        import aws_sdk_personalize.types.ranking_influence_type

        out[
            aws_sdk_personalize.types.ranking_influence_type.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out
