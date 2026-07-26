"""Generated from Smithy shape ``com.amazonaws.glue#CodeGenConfigurationNodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.code_gen_configuration_node
    import capo_glue.types.node_id

CodeGenConfigurationNodes: TypeAlias = dict[
    "capo_glue.types.node_id.NodeId",
    "capo_glue.types.code_gen_configuration_node.CodeGenConfigurationNode",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CodeGenConfigurationNodes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.code_gen_configuration_node

        out[key] = capo_glue.types.code_gen_configuration_node.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeGenConfigurationNodes:
    out: CodeGenConfigurationNodes = {}
    for key, value in data.items():
        import capo_glue.types.code_gen_configuration_node

        out[key] = capo_glue.types.code_gen_configuration_node.deserialize_aws_json_1_1(
            value
        )
    return out
