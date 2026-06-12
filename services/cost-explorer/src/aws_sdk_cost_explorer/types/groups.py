"""Generated from Smithy shape ``com.amazonaws.costexplorer#Groups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.group

Groups: TypeAlias = list["aws_sdk_cost_explorer.types.group.Group"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Groups) -> list:
    import aws_sdk_cost_explorer.types.group

    out: list = []
    for item in value:
        out.append(aws_sdk_cost_explorer.types.group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Groups:
    import aws_sdk_cost_explorer.types.group

    out: Groups = []
    for item in data:
        out.append(aws_sdk_cost_explorer.types.group.deserialize_aws_json_1_1(item))
    return out
