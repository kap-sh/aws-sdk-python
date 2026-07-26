"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RuleMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.rule
    import capo_clouddirectory.types.rule_key

RuleMap: TypeAlias = dict[
    "capo_clouddirectory.types.rule_key.RuleKey", "capo_clouddirectory.types.rule.Rule"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RuleMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_clouddirectory.types.rule

        out[key] = capo_clouddirectory.types.rule.serialize_json(value)
    return out


def deserialize_json(data: dict) -> RuleMap:
    out: RuleMap = {}
    for key, value in data.items():
        import capo_clouddirectory.types.rule

        out[key] = capo_clouddirectory.types.rule.deserialize_json(value)
    return out
