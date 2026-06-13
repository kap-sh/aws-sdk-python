"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MembershipInferenceAttackScore``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.membership_inference_attack_version


class MembershipInferenceAttackScore(TypedDict):
    attack_version: "aws_sdk_cleanroomsml.types.membership_inference_attack_version.MembershipInferenceAttackVersion"
    """<p>The version of the membership inference attack, which consists of the attack type and its version number, used to generate this privacy score.</p>"""
    score: "float"
    """<p>The numerical score representing the vulnerability to membership inference attacks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipInferenceAttackScore) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.membership_inference_attack_version

    out["attackVersion"] = (
        aws_sdk_cleanroomsml.types.membership_inference_attack_version.serialize_json(
            value["attack_version"]
        )
    )
    out["score"] = value["score"]
    return out


def deserialize_json(data: dict) -> MembershipInferenceAttackScore:
    out: MembershipInferenceAttackScore = {}  # type: ignore[typeddict-item]
    if "attackVersion" in data:
        import aws_sdk_cleanroomsml.types.membership_inference_attack_version

        out["attack_version"] = (
            aws_sdk_cleanroomsml.types.membership_inference_attack_version.deserialize_json(
                data["attackVersion"]
            )
        )
    else:
        raise DeserializationError(
            "MembershipInferenceAttackScore.attack_version required"
        )
    if "score" in data:
        out["score"] = data["score"]
    else:
        raise DeserializationError("MembershipInferenceAttackScore.score required")
    return out
