"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RuleTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.rule_tag

RuleTags: TypeAlias = list["capo_codeguru_reviewer.types.rule_tag.RuleTag"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleTags) -> list:
    return list(value)


def deserialize_json(data: list) -> RuleTags:
    return list(data)
