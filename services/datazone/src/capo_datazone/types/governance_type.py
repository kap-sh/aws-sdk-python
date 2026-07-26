"""Generated from Smithy shape ``com.amazonaws.datazone#GovernanceType``."""

from typing import Literal, TypeAlias, cast

GovernanceType: TypeAlias = Literal[
    "AWS_MANAGED",
    "USER_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GovernanceType) -> str:
    return value


def deserialize_json(data: str) -> GovernanceType:
    return cast(GovernanceType, data)
