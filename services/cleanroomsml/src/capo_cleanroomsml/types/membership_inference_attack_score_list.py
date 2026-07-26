"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MembershipInferenceAttackScoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.membership_inference_attack_score

MembershipInferenceAttackScoreList: TypeAlias = list[
    "capo_cleanroomsml.types.membership_inference_attack_score.MembershipInferenceAttackScore"
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipInferenceAttackScoreList) -> list:
    import capo_cleanroomsml.types.membership_inference_attack_score

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.membership_inference_attack_score.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MembershipInferenceAttackScoreList:
    import capo_cleanroomsml.types.membership_inference_attack_score

    out: MembershipInferenceAttackScoreList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.membership_inference_attack_score.deserialize_json(
                item
            )
        )
    return out
