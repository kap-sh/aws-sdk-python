"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StringListValidation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.allowed_string_list_values_list


class StringListValidation(TypedDict):
    allowed_values: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.allowed_string_list_values_list.AllowedStringListValuesList"
    ]
    """<p>Allowed values for items in this STRINGLIST field.</p>"""
    max_items: NotRequired["int"]
    """<p>Maximum number of items in the string list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringListValidation) -> dict:
    out: dict = {}
    if "allowed_values" in value:
        import aws_sdk_bedrock_agentcore_control.types.allowed_string_list_values_list

        out["allowedValues"] = (
            aws_sdk_bedrock_agentcore_control.types.allowed_string_list_values_list.serialize_json(
                value["allowed_values"]
            )
        )
    if "max_items" in value:
        out["maxItems"] = value["max_items"]
    return out


def deserialize_json(data: dict) -> StringListValidation:
    out: StringListValidation = {}  # type: ignore[typeddict-item]
    if "allowedValues" in data:
        import aws_sdk_bedrock_agentcore_control.types.allowed_string_list_values_list

        out["allowed_values"] = (
            aws_sdk_bedrock_agentcore_control.types.allowed_string_list_values_list.deserialize_json(
                data["allowedValues"]
            )
        )
    if "maxItems" in data:
        out["max_items"] = data["maxItems"]
    return out
