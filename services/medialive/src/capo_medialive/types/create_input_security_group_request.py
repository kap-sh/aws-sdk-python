"""Generated from Smithy shape ``com.amazonaws.medialive#CreateInputSecurityGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_input_whitelist_rule_cidr
    import capo_medialive.types.tags


class CreateInputSecurityGroupRequest(TypedDict, closed=True):
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    whitelist_rules: NotRequired[
        "capo_medialive.types.__list_of_input_whitelist_rule_cidr.__listOfInputWhitelistRuleCidr"
    ]
    """List of IPv4 CIDR addresses to whitelist"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputSecurityGroupRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    if "whitelist_rules" in value:
        import capo_medialive.types.__list_of_input_whitelist_rule_cidr

        out["whitelistRules"] = (
            capo_medialive.types.__list_of_input_whitelist_rule_cidr.serialize_json(
                value["whitelist_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateInputSecurityGroupRequest:
    out: CreateInputSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    if "whitelistRules" in data:
        import capo_medialive.types.__list_of_input_whitelist_rule_cidr

        out["whitelist_rules"] = (
            capo_medialive.types.__list_of_input_whitelist_rule_cidr.deserialize_json(
                data["whitelistRules"]
            )
        )
    return out
