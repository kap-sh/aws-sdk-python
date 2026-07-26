"""Generated from Smithy shape ``com.amazonaws.inspector#ResourceGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.resource_group

ResourceGroupList: TypeAlias = list["capo_inspector.types.resource_group.ResourceGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceGroupList) -> list:
    import capo_inspector.types.resource_group

    out: list = []
    for item in value:
        out.append(capo_inspector.types.resource_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceGroupList:
    import capo_inspector.types.resource_group

    out: ResourceGroupList = []
    for item in data:
        out.append(capo_inspector.types.resource_group.deserialize_aws_json_1_1(item))
    return out
