"""Generated from Smithy shape ``com.amazonaws.costexplorer#GroupDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.group_definition_key
    import capo_cost_explorer.types.group_definition_type


class GroupDefinition(TypedDict, closed=True):
    type: NotRequired[
        "capo_cost_explorer.types.group_definition_type.GroupDefinitionType"
    ]
    """<p>The string that represents the type of group.</p>"""
    key: NotRequired["capo_cost_explorer.types.group_definition_key.GroupDefinitionKey"]
    """<p>The string that represents a key for a specified group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupDefinition) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_cost_explorer.types.group_definition_type

        out["Type"] = (
            capo_cost_explorer.types.group_definition_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "key" in value:
        out["Key"] = value["key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupDefinition:
    out: GroupDefinition = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_cost_explorer.types.group_definition_type

        out["type"] = (
            capo_cost_explorer.types.group_definition_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Key" in data:
        out["key"] = data["Key"]
    return out
