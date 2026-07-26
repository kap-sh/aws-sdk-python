"""Generated from Smithy shape ``com.amazonaws.databrew#RuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.rule

RuleList: TypeAlias = list["capo_databrew.types.rule.Rule"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleList) -> list:
    import capo_databrew.types.rule

    out: list = []
    for item in value:
        out.append(capo_databrew.types.rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleList:
    import capo_databrew.types.rule

    out: RuleList = []
    for item in data:
        out.append(capo_databrew.types.rule.deserialize_json(item))
    return out
