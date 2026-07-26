"""Generated from Smithy shape ``com.amazonaws.invoicing#ResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.resource_tag

ResourceTagList: TypeAlias = list["capo_invoicing.types.resource_tag.ResourceTag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTagList) -> list:
    import capo_invoicing.types.resource_tag

    out: list = []
    for item in value:
        out.append(capo_invoicing.types.resource_tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceTagList:
    import capo_invoicing.types.resource_tag

    out: ResourceTagList = []
    for item in data:
        out.append(capo_invoicing.types.resource_tag.deserialize_aws_json_1_0(item))
    return out
