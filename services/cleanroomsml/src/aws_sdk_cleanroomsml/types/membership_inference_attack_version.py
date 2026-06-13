"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MembershipInferenceAttackVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

MembershipInferenceAttackVersion: TypeAlias = Literal["DISTANCE_TO_CLOSEST_RECORD_V1",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DISTANCE_TO_CLOSEST_RECORD_V1",))


def serialize_json(value: MembershipInferenceAttackVersion) -> str:
    return value


def deserialize_json(data: str) -> MembershipInferenceAttackVersion:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MembershipInferenceAttackVersion value: {data!r}"
        )
    return cast(MembershipInferenceAttackVersion, data)
