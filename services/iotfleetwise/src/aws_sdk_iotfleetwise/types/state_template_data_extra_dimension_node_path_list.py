"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateDataExtraDimensionNodePathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.node_path

StateTemplateDataExtraDimensionNodePathList: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.node_path.NodePath"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateDataExtraDimensionNodePathList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StateTemplateDataExtraDimensionNodePathList:
    return list(data)
