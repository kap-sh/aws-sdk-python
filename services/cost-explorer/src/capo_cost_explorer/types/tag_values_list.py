"""Generated from Smithy shape ``com.amazonaws.costexplorer#TagValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.tag_values

TagValuesList: TypeAlias = list["capo_cost_explorer.types.tag_values.TagValues"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagValuesList) -> list:
    import capo_cost_explorer.types.tag_values

    out: list = []
    for item in value:
        out.append(capo_cost_explorer.types.tag_values.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagValuesList:
    import capo_cost_explorer.types.tag_values

    out: TagValuesList = []
    for item in data:
        out.append(capo_cost_explorer.types.tag_values.deserialize_aws_json_1_1(item))
    return out
