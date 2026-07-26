"""Generated from Smithy shape ``com.amazonaws.entityresolution#RuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.rule

RuleList: TypeAlias = list["capo_entityresolution.types.rule.Rule"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleList) -> list:
    import capo_entityresolution.types.rule

    out: list = []
    for item in value:
        out.append(capo_entityresolution.types.rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleList:
    import capo_entityresolution.types.rule

    out: RuleList = []
    for item in data:
        out.append(capo_entityresolution.types.rule.deserialize_json(item))
    return out
