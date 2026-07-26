"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PolicyExistenceCondition``."""

from typing import Literal, TypeAlias, cast

PolicyExistenceCondition: TypeAlias = Literal[
    "POLICY_MUST_EXIST",
    "POLICY_MUST_NOT_EXIST",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyExistenceCondition) -> str:
    return value


def deserialize_json(data: str) -> PolicyExistenceCondition:
    return cast(PolicyExistenceCondition, data)
