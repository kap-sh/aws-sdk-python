"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.node_path

StateTemplateProperties: TypeAlias = list["capo_iotfleetwise.types.node_path.NodePath"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateProperties) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StateTemplateProperties:
    return list(data)
