"""Generated from Smithy shape ``com.amazonaws.codecommit#ReactionCountsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.count
    import capo_codecommit.types.reaction_value

ReactionCountsMap: TypeAlias = dict[
    "capo_codecommit.types.reaction_value.ReactionValue",
    "capo_codecommit.types.count.Count",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ReactionCountsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ReactionCountsMap:
    out: ReactionCountsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
