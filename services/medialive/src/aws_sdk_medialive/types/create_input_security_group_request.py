"""Generated from Smithy shape ``com.amazonaws.medialive#CreateInputSecurityGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr
    import aws_sdk_medialive.types.tags


class CreateInputSecurityGroupRequest(TypedDict):
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    whitelist_rules: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr.__listOfInputWhitelistRuleCidr"
    ]
    """List of IPv4 CIDR addresses to whitelist"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputSecurityGroupRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    if "whitelist_rules" in value:
        import aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr

        out["whitelistRules"] = (
            aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr.serialize_json(
                value["whitelist_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateInputSecurityGroupRequest:
    out: CreateInputSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    if "whitelistRules" in data:
        import aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr

        out["whitelist_rules"] = (
            aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr.deserialize_json(
                data["whitelistRules"]
            )
        )
    return out
