"""Generated from Smithy shape ``com.amazonaws.datazone#RuleTargetType``."""

from typing import Literal, TypeAlias, cast

RuleTargetType: TypeAlias = Literal["DOMAIN_UNIT",]


# --- restJson1 ser/de ---
def serialize_json(value: RuleTargetType) -> str:
    return value


def deserialize_json(data: str) -> RuleTargetType:
    return cast(RuleTargetType, data)
