"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateMetadataExtraDimensionNodePathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.node_path

StateTemplateMetadataExtraDimensionNodePathList: TypeAlias = list[
    "capo_iotfleetwise.types.node_path.NodePath"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: StateTemplateMetadataExtraDimensionNodePathList,
) -> list:
    return list(value)


def deserialize_aws_json_1_0(
    data: list,
) -> StateTemplateMetadataExtraDimensionNodePathList:
    return list(data)
