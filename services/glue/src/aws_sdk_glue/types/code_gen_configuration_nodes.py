"""Generated from Smithy shape ``com.amazonaws.glue#CodeGenConfigurationNodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.code_gen_configuration_node
    import aws_sdk_glue.types.node_id

CodeGenConfigurationNodes: TypeAlias = dict[
    "aws_sdk_glue.types.node_id.NodeId",
    "aws_sdk_glue.types.code_gen_configuration_node.CodeGenConfigurationNode",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CodeGenConfigurationNodes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_glue.types.code_gen_configuration_node

        out[key] = (
            aws_sdk_glue.types.code_gen_configuration_node.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeGenConfigurationNodes:
    out: CodeGenConfigurationNodes = {}
    for key, value in data.items():
        import aws_sdk_glue.types.code_gen_configuration_node

        out[key] = (
            aws_sdk_glue.types.code_gen_configuration_node.deserialize_aws_json_1_1(
                value
            )
        )
    return out
