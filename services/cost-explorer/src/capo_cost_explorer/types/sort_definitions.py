"""Generated from Smithy shape ``com.amazonaws.costexplorer#SortDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.sort_definition

SortDefinitions: TypeAlias = list[
    "capo_cost_explorer.types.sort_definition.SortDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortDefinitions) -> list:
    import capo_cost_explorer.types.sort_definition

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.sort_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SortDefinitions:
    import capo_cost_explorer.types.sort_definition

    out: SortDefinitions = []
    for item in data:
        out.append(
            capo_cost_explorer.types.sort_definition.deserialize_aws_json_1_1(item)
        )
    return out
