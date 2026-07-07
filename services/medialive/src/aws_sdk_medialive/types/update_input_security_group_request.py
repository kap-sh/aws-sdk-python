"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateInputSecurityGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.tags


class UpdateInputSecurityGroupRequest(TypedDict, closed=True):
    input_security_group_id: "aws_sdk_medialive.types.__string.__string"
    """The id of the Input Security Group to update."""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    whitelist_rules: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_whitelist_rule_cidr.__listOfInputWhitelistRuleCidr"
    ]
    """List of IPv4 CIDR addresses to whitelist"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInputSecurityGroupRequest) -> dict:
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


def deserialize_json(data: dict) -> UpdateInputSecurityGroupRequest:
    out: UpdateInputSecurityGroupRequest = {}  # type: ignore[typeddict-item]
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
