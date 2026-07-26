"""Generated from Smithy shape ``com.amazonaws.dax#NodeTypeSpecificValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dax.types.node_type_specific_value

NodeTypeSpecificValueList: TypeAlias = list[
    "capo_dax.types.node_type_specific_value.NodeTypeSpecificValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeTypeSpecificValueList) -> list:
    import capo_dax.types.node_type_specific_value

    out: list = []
    for item in value:
        out.append(capo_dax.types.node_type_specific_value.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NodeTypeSpecificValueList:
    import capo_dax.types.node_type_specific_value

    out: NodeTypeSpecificValueList = []
    for item in data:
        out.append(
            capo_dax.types.node_type_specific_value.deserialize_aws_json_1_1(item)
        )
    return out
