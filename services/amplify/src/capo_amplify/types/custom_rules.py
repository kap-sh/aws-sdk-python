"""Generated from Smithy shape ``com.amazonaws.amplify#CustomRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.custom_rule

CustomRules: TypeAlias = list["capo_amplify.types.custom_rule.CustomRule"]


# --- restJson1 ser/de ---
def serialize_json(value: CustomRules) -> list:
    import capo_amplify.types.custom_rule

    out: list = []
    for item in value:
        out.append(capo_amplify.types.custom_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomRules:
    import capo_amplify.types.custom_rule

    out: CustomRules = []
    for item in data:
        out.append(capo_amplify.types.custom_rule.deserialize_json(item))
    return out
