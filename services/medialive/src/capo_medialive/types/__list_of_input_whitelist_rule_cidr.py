"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputWhitelistRuleCidr``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.input_whitelist_rule_cidr

__listOfInputWhitelistRuleCidr: TypeAlias = list[
    "capo_medialive.types.input_whitelist_rule_cidr.InputWhitelistRuleCidr"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputWhitelistRuleCidr) -> list:
    import capo_medialive.types.input_whitelist_rule_cidr

    out: list = []
    for item in value:
        out.append(capo_medialive.types.input_whitelist_rule_cidr.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputWhitelistRuleCidr:
    import capo_medialive.types.input_whitelist_rule_cidr

    out: __listOfInputWhitelistRuleCidr = []
    for item in data:
        out.append(
            capo_medialive.types.input_whitelist_rule_cidr.deserialize_json(item)
        )
    return out
