"""Generated from Smithy shape ``com.amazonaws.medialive#InputSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__list_of_input_whitelist_rule
    import capo_medialive.types.__string
    import capo_medialive.types.input_security_group_state
    import capo_medialive.types.tags


class InputSecurityGroup(TypedDict, closed=True):
    arn: NotRequired["capo_medialive.types.__string.__string"]
    """Unique ARN of Input Security Group"""
    id: NotRequired["capo_medialive.types.__string.__string"]
    """The Id of the Input Security Group"""
    inputs: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """The list of inputs currently using this Input Security Group."""
    state: NotRequired[
        "capo_medialive.types.input_security_group_state.InputSecurityGroupState"
    ]
    """The current state of the Input Security Group."""
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    whitelist_rules: NotRequired[
        "capo_medialive.types.__list_of_input_whitelist_rule.__listOfInputWhitelistRule"
    ]
    """Whitelist rules and their sync status"""
    channels: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """The list of channels currently using this Input Security Group as their channel security group."""


# --- restJson1 ser/de ---
def serialize_json(value: InputSecurityGroup) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "inputs" in value:
        import capo_medialive.types.__list_of__string

        out["inputs"] = capo_medialive.types.__list_of__string.serialize_json(
            value["inputs"]
        )
    if "state" in value:
        import capo_medialive.types.input_security_group_state

        out["state"] = capo_medialive.types.input_security_group_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    if "whitelist_rules" in value:
        import capo_medialive.types.__list_of_input_whitelist_rule

        out["whitelistRules"] = (
            capo_medialive.types.__list_of_input_whitelist_rule.serialize_json(
                value["whitelist_rules"]
            )
        )
    if "channels" in value:
        import capo_medialive.types.__list_of__string

        out["channels"] = capo_medialive.types.__list_of__string.serialize_json(
            value["channels"]
        )
    return out


def deserialize_json(data: dict) -> InputSecurityGroup:
    out: InputSecurityGroup = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "inputs" in data:
        import capo_medialive.types.__list_of__string

        out["inputs"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["inputs"]
        )
    if "state" in data:
        import capo_medialive.types.input_security_group_state

        out["state"] = capo_medialive.types.input_security_group_state.deserialize_json(
            data["state"]
        )
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    if "whitelistRules" in data:
        import capo_medialive.types.__list_of_input_whitelist_rule

        out["whitelist_rules"] = (
            capo_medialive.types.__list_of_input_whitelist_rule.deserialize_json(
                data["whitelistRules"]
            )
        )
    if "channels" in data:
        import capo_medialive.types.__list_of__string

        out["channels"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["channels"]
        )
    return out
