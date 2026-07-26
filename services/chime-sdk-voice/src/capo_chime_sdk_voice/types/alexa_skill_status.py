"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#AlexaSkillStatus``."""

from typing import Literal, TypeAlias, cast

AlexaSkillStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AlexaSkillStatus) -> str:
    return value


def deserialize_json(data: str) -> AlexaSkillStatus:
    return cast(AlexaSkillStatus, data)
