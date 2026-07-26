"""Generated from Smithy shape ``com.amazonaws.efs#TransitionToPrimaryStorageClassRules``."""

from typing import Literal, TypeAlias, cast

TransitionToPrimaryStorageClassRules: TypeAlias = Literal["AFTER_1_ACCESS",]


# --- restJson1 ser/de ---
def serialize_json(value: TransitionToPrimaryStorageClassRules) -> str:
    return value


def deserialize_json(data: str) -> TransitionToPrimaryStorageClassRules:
    return cast(TransitionToPrimaryStorageClassRules, data)
