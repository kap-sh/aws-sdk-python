"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MembershipInferenceAttackVersion``."""

from typing import Literal, TypeAlias, cast

MembershipInferenceAttackVersion: TypeAlias = Literal["DISTANCE_TO_CLOSEST_RECORD_V1",]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipInferenceAttackVersion) -> str:
    return value


def deserialize_json(data: str) -> MembershipInferenceAttackVersion:
    return cast(MembershipInferenceAttackVersion, data)
