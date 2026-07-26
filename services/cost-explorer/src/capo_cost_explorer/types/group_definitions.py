"""Generated from Smithy shape ``com.amazonaws.costexplorer#GroupDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.group_definition

GroupDefinitions: TypeAlias = list[
    "capo_cost_explorer.types.group_definition.GroupDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupDefinitions) -> list:
    import capo_cost_explorer.types.group_definition

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.group_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupDefinitions:
    import capo_cost_explorer.types.group_definition

    out: GroupDefinitions = []
    for item in data:
        out.append(
            capo_cost_explorer.types.group_definition.deserialize_aws_json_1_1(item)
        )
    return out
