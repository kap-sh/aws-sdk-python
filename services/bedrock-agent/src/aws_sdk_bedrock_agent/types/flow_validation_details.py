"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidationDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.cyclic_connection_flow_validation_details
    import aws_sdk_bedrock_agent.types.duplicate_condition_expression_flow_validation_details
    import aws_sdk_bedrock_agent.types.duplicate_connections_flow_validation_details
    import aws_sdk_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details
    import aws_sdk_bedrock_agent.types.invalid_loop_boundary_flow_validation_details
    import aws_sdk_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details
    import aws_sdk_bedrock_agent.types.malformed_condition_expression_flow_validation_details
    import aws_sdk_bedrock_agent.types.malformed_node_input_expression_flow_validation_details
    import aws_sdk_bedrock_agent.types.mismatched_node_input_type_flow_validation_details
    import aws_sdk_bedrock_agent.types.mismatched_node_output_type_flow_validation_details
    import aws_sdk_bedrock_agent.types.missing_connection_configuration_flow_validation_details
    import aws_sdk_bedrock_agent.types.missing_default_condition_flow_validation_details
    import aws_sdk_bedrock_agent.types.missing_ending_nodes_flow_validation_details
    import aws_sdk_bedrock_agent.types.missing_loop_controller_node_flow_validation_details
    import aws_sdk_bedrock_agent.types.missing_loop_input_node_flow_validation_details
    import aws_sdk_bedrock_agent.types.missing_node_configuration_flow_validation_details
    import aws_sdk_bedrock_agent.types.missing_node_input_flow_validation_details
    import aws_sdk_bedrock_agent.types.missing_node_output_flow_validation_details
    import aws_sdk_bedrock_agent.types.missing_starting_nodes_flow_validation_details
    import aws_sdk_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details
    import aws_sdk_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details
    import aws_sdk_bedrock_agent.types.multiple_node_input_connections_flow_validation_details
    import aws_sdk_bedrock_agent.types.unfulfilled_node_input_flow_validation_details
    import aws_sdk_bedrock_agent.types.unknown_connection_condition_flow_validation_details
    import aws_sdk_bedrock_agent.types.unknown_connection_source_flow_validation_details
    import aws_sdk_bedrock_agent.types.unknown_connection_source_output_flow_validation_details
    import aws_sdk_bedrock_agent.types.unknown_connection_target_flow_validation_details
    import aws_sdk_bedrock_agent.types.unknown_connection_target_input_flow_validation_details
    import aws_sdk_bedrock_agent.types.unknown_node_input_flow_validation_details
    import aws_sdk_bedrock_agent.types.unknown_node_output_flow_validation_details
    import aws_sdk_bedrock_agent.types.unreachable_node_flow_validation_details
    import aws_sdk_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details
    import aws_sdk_bedrock_agent.types.unspecified_flow_validation_details


class _FlowValidationDetails_cyclicConnection(TypedDict):
    cyclicConnection: "aws_sdk_bedrock_agent.types.cyclic_connection_flow_validation_details.CyclicConnectionFlowValidationDetails"


class _FlowValidationDetails_duplicateConnections(TypedDict):
    duplicateConnections: "aws_sdk_bedrock_agent.types.duplicate_connections_flow_validation_details.DuplicateConnectionsFlowValidationDetails"


class _FlowValidationDetails_duplicateConditionExpression(TypedDict):
    duplicateConditionExpression: "aws_sdk_bedrock_agent.types.duplicate_condition_expression_flow_validation_details.DuplicateConditionExpressionFlowValidationDetails"


class _FlowValidationDetails_unreachableNode(TypedDict):
    unreachableNode: "aws_sdk_bedrock_agent.types.unreachable_node_flow_validation_details.UnreachableNodeFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionSource(TypedDict):
    unknownConnectionSource: "aws_sdk_bedrock_agent.types.unknown_connection_source_flow_validation_details.UnknownConnectionSourceFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionSourceOutput(TypedDict):
    unknownConnectionSourceOutput: "aws_sdk_bedrock_agent.types.unknown_connection_source_output_flow_validation_details.UnknownConnectionSourceOutputFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionTarget(TypedDict):
    unknownConnectionTarget: "aws_sdk_bedrock_agent.types.unknown_connection_target_flow_validation_details.UnknownConnectionTargetFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionTargetInput(TypedDict):
    unknownConnectionTargetInput: "aws_sdk_bedrock_agent.types.unknown_connection_target_input_flow_validation_details.UnknownConnectionTargetInputFlowValidationDetails"


class _FlowValidationDetails_unknownConnectionCondition(TypedDict):
    unknownConnectionCondition: "aws_sdk_bedrock_agent.types.unknown_connection_condition_flow_validation_details.UnknownConnectionConditionFlowValidationDetails"


class _FlowValidationDetails_malformedConditionExpression(TypedDict):
    malformedConditionExpression: "aws_sdk_bedrock_agent.types.malformed_condition_expression_flow_validation_details.MalformedConditionExpressionFlowValidationDetails"


class _FlowValidationDetails_malformedNodeInputExpression(TypedDict):
    malformedNodeInputExpression: "aws_sdk_bedrock_agent.types.malformed_node_input_expression_flow_validation_details.MalformedNodeInputExpressionFlowValidationDetails"


class _FlowValidationDetails_mismatchedNodeInputType(TypedDict):
    mismatchedNodeInputType: "aws_sdk_bedrock_agent.types.mismatched_node_input_type_flow_validation_details.MismatchedNodeInputTypeFlowValidationDetails"


class _FlowValidationDetails_mismatchedNodeOutputType(TypedDict):
    mismatchedNodeOutputType: "aws_sdk_bedrock_agent.types.mismatched_node_output_type_flow_validation_details.MismatchedNodeOutputTypeFlowValidationDetails"


class _FlowValidationDetails_incompatibleConnectionDataType(TypedDict):
    incompatibleConnectionDataType: "aws_sdk_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details.IncompatibleConnectionDataTypeFlowValidationDetails"


class _FlowValidationDetails_missingConnectionConfiguration(TypedDict):
    missingConnectionConfiguration: "aws_sdk_bedrock_agent.types.missing_connection_configuration_flow_validation_details.MissingConnectionConfigurationFlowValidationDetails"


class _FlowValidationDetails_missingDefaultCondition(TypedDict):
    missingDefaultCondition: "aws_sdk_bedrock_agent.types.missing_default_condition_flow_validation_details.MissingDefaultConditionFlowValidationDetails"


class _FlowValidationDetails_missingEndingNodes(TypedDict):
    missingEndingNodes: "aws_sdk_bedrock_agent.types.missing_ending_nodes_flow_validation_details.MissingEndingNodesFlowValidationDetails"


class _FlowValidationDetails_missingNodeConfiguration(TypedDict):
    missingNodeConfiguration: "aws_sdk_bedrock_agent.types.missing_node_configuration_flow_validation_details.MissingNodeConfigurationFlowValidationDetails"


class _FlowValidationDetails_missingNodeInput(TypedDict):
    missingNodeInput: "aws_sdk_bedrock_agent.types.missing_node_input_flow_validation_details.MissingNodeInputFlowValidationDetails"


class _FlowValidationDetails_missingNodeOutput(TypedDict):
    missingNodeOutput: "aws_sdk_bedrock_agent.types.missing_node_output_flow_validation_details.MissingNodeOutputFlowValidationDetails"


class _FlowValidationDetails_missingStartingNodes(TypedDict):
    missingStartingNodes: "aws_sdk_bedrock_agent.types.missing_starting_nodes_flow_validation_details.MissingStartingNodesFlowValidationDetails"


class _FlowValidationDetails_multipleNodeInputConnections(TypedDict):
    multipleNodeInputConnections: "aws_sdk_bedrock_agent.types.multiple_node_input_connections_flow_validation_details.MultipleNodeInputConnectionsFlowValidationDetails"


class _FlowValidationDetails_unfulfilledNodeInput(TypedDict):
    unfulfilledNodeInput: "aws_sdk_bedrock_agent.types.unfulfilled_node_input_flow_validation_details.UnfulfilledNodeInputFlowValidationDetails"


class _FlowValidationDetails_unsatisfiedConnectionConditions(TypedDict):
    unsatisfiedConnectionConditions: "aws_sdk_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details.UnsatisfiedConnectionConditionsFlowValidationDetails"


class _FlowValidationDetails_unspecified(TypedDict):
    unspecified: "aws_sdk_bedrock_agent.types.unspecified_flow_validation_details.UnspecifiedFlowValidationDetails"


class _FlowValidationDetails_unknownNodeInput(TypedDict):
    unknownNodeInput: "aws_sdk_bedrock_agent.types.unknown_node_input_flow_validation_details.UnknownNodeInputFlowValidationDetails"


class _FlowValidationDetails_unknownNodeOutput(TypedDict):
    unknownNodeOutput: "aws_sdk_bedrock_agent.types.unknown_node_output_flow_validation_details.UnknownNodeOutputFlowValidationDetails"


class _FlowValidationDetails_missingLoopInputNode(TypedDict):
    missingLoopInputNode: "aws_sdk_bedrock_agent.types.missing_loop_input_node_flow_validation_details.MissingLoopInputNodeFlowValidationDetails"


class _FlowValidationDetails_missingLoopControllerNode(TypedDict):
    missingLoopControllerNode: "aws_sdk_bedrock_agent.types.missing_loop_controller_node_flow_validation_details.MissingLoopControllerNodeFlowValidationDetails"


class _FlowValidationDetails_multipleLoopInputNodes(TypedDict):
    multipleLoopInputNodes: "aws_sdk_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details.MultipleLoopInputNodesFlowValidationDetails"


class _FlowValidationDetails_multipleLoopControllerNodes(TypedDict):
    multipleLoopControllerNodes: "aws_sdk_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details.MultipleLoopControllerNodesFlowValidationDetails"


class _FlowValidationDetails_loopIncompatibleNodeType(TypedDict):
    loopIncompatibleNodeType: "aws_sdk_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details.LoopIncompatibleNodeTypeFlowValidationDetails"


class _FlowValidationDetails_invalidLoopBoundary(TypedDict):
    invalidLoopBoundary: "aws_sdk_bedrock_agent.types.invalid_loop_boundary_flow_validation_details.InvalidLoopBoundaryFlowValidationDetails"


FlowValidationDetails: TypeAlias = (
    _FlowValidationDetails_cyclicConnection
    | _FlowValidationDetails_duplicateConnections
    | _FlowValidationDetails_duplicateConditionExpression
    | _FlowValidationDetails_unreachableNode
    | _FlowValidationDetails_unknownConnectionSource
    | _FlowValidationDetails_unknownConnectionSourceOutput
    | _FlowValidationDetails_unknownConnectionTarget
    | _FlowValidationDetails_unknownConnectionTargetInput
    | _FlowValidationDetails_unknownConnectionCondition
    | _FlowValidationDetails_malformedConditionExpression
    | _FlowValidationDetails_malformedNodeInputExpression
    | _FlowValidationDetails_mismatchedNodeInputType
    | _FlowValidationDetails_mismatchedNodeOutputType
    | _FlowValidationDetails_incompatibleConnectionDataType
    | _FlowValidationDetails_missingConnectionConfiguration
    | _FlowValidationDetails_missingDefaultCondition
    | _FlowValidationDetails_missingEndingNodes
    | _FlowValidationDetails_missingNodeConfiguration
    | _FlowValidationDetails_missingNodeInput
    | _FlowValidationDetails_missingNodeOutput
    | _FlowValidationDetails_missingStartingNodes
    | _FlowValidationDetails_multipleNodeInputConnections
    | _FlowValidationDetails_unfulfilledNodeInput
    | _FlowValidationDetails_unsatisfiedConnectionConditions
    | _FlowValidationDetails_unspecified
    | _FlowValidationDetails_unknownNodeInput
    | _FlowValidationDetails_unknownNodeOutput
    | _FlowValidationDetails_missingLoopInputNode
    | _FlowValidationDetails_missingLoopControllerNode
    | _FlowValidationDetails_multipleLoopInputNodes
    | _FlowValidationDetails_multipleLoopControllerNodes
    | _FlowValidationDetails_loopIncompatibleNodeType
    | _FlowValidationDetails_invalidLoopBoundary
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowValidationDetails) -> dict:
    if "cyclicConnection" in value:
        import aws_sdk_bedrock_agent.types.cyclic_connection_flow_validation_details

        return {
            "cyclicConnection": aws_sdk_bedrock_agent.types.cyclic_connection_flow_validation_details.serialize_json(
                value["cyclicConnection"]
            )
        }
    elif "duplicateConnections" in value:
        import aws_sdk_bedrock_agent.types.duplicate_connections_flow_validation_details

        return {
            "duplicateConnections": aws_sdk_bedrock_agent.types.duplicate_connections_flow_validation_details.serialize_json(
                value["duplicateConnections"]
            )
        }
    elif "duplicateConditionExpression" in value:
        import aws_sdk_bedrock_agent.types.duplicate_condition_expression_flow_validation_details

        return {
            "duplicateConditionExpression": aws_sdk_bedrock_agent.types.duplicate_condition_expression_flow_validation_details.serialize_json(
                value["duplicateConditionExpression"]
            )
        }
    elif "unreachableNode" in value:
        import aws_sdk_bedrock_agent.types.unreachable_node_flow_validation_details

        return {
            "unreachableNode": aws_sdk_bedrock_agent.types.unreachable_node_flow_validation_details.serialize_json(
                value["unreachableNode"]
            )
        }
    elif "unknownConnectionSource" in value:
        import aws_sdk_bedrock_agent.types.unknown_connection_source_flow_validation_details

        return {
            "unknownConnectionSource": aws_sdk_bedrock_agent.types.unknown_connection_source_flow_validation_details.serialize_json(
                value["unknownConnectionSource"]
            )
        }
    elif "unknownConnectionSourceOutput" in value:
        import aws_sdk_bedrock_agent.types.unknown_connection_source_output_flow_validation_details

        return {
            "unknownConnectionSourceOutput": aws_sdk_bedrock_agent.types.unknown_connection_source_output_flow_validation_details.serialize_json(
                value["unknownConnectionSourceOutput"]
            )
        }
    elif "unknownConnectionTarget" in value:
        import aws_sdk_bedrock_agent.types.unknown_connection_target_flow_validation_details

        return {
            "unknownConnectionTarget": aws_sdk_bedrock_agent.types.unknown_connection_target_flow_validation_details.serialize_json(
                value["unknownConnectionTarget"]
            )
        }
    elif "unknownConnectionTargetInput" in value:
        import aws_sdk_bedrock_agent.types.unknown_connection_target_input_flow_validation_details

        return {
            "unknownConnectionTargetInput": aws_sdk_bedrock_agent.types.unknown_connection_target_input_flow_validation_details.serialize_json(
                value["unknownConnectionTargetInput"]
            )
        }
    elif "unknownConnectionCondition" in value:
        import aws_sdk_bedrock_agent.types.unknown_connection_condition_flow_validation_details

        return {
            "unknownConnectionCondition": aws_sdk_bedrock_agent.types.unknown_connection_condition_flow_validation_details.serialize_json(
                value["unknownConnectionCondition"]
            )
        }
    elif "malformedConditionExpression" in value:
        import aws_sdk_bedrock_agent.types.malformed_condition_expression_flow_validation_details

        return {
            "malformedConditionExpression": aws_sdk_bedrock_agent.types.malformed_condition_expression_flow_validation_details.serialize_json(
                value["malformedConditionExpression"]
            )
        }
    elif "malformedNodeInputExpression" in value:
        import aws_sdk_bedrock_agent.types.malformed_node_input_expression_flow_validation_details

        return {
            "malformedNodeInputExpression": aws_sdk_bedrock_agent.types.malformed_node_input_expression_flow_validation_details.serialize_json(
                value["malformedNodeInputExpression"]
            )
        }
    elif "mismatchedNodeInputType" in value:
        import aws_sdk_bedrock_agent.types.mismatched_node_input_type_flow_validation_details

        return {
            "mismatchedNodeInputType": aws_sdk_bedrock_agent.types.mismatched_node_input_type_flow_validation_details.serialize_json(
                value["mismatchedNodeInputType"]
            )
        }
    elif "mismatchedNodeOutputType" in value:
        import aws_sdk_bedrock_agent.types.mismatched_node_output_type_flow_validation_details

        return {
            "mismatchedNodeOutputType": aws_sdk_bedrock_agent.types.mismatched_node_output_type_flow_validation_details.serialize_json(
                value["mismatchedNodeOutputType"]
            )
        }
    elif "incompatibleConnectionDataType" in value:
        import aws_sdk_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details

        return {
            "incompatibleConnectionDataType": aws_sdk_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details.serialize_json(
                value["incompatibleConnectionDataType"]
            )
        }
    elif "missingConnectionConfiguration" in value:
        import aws_sdk_bedrock_agent.types.missing_connection_configuration_flow_validation_details

        return {
            "missingConnectionConfiguration": aws_sdk_bedrock_agent.types.missing_connection_configuration_flow_validation_details.serialize_json(
                value["missingConnectionConfiguration"]
            )
        }
    elif "missingDefaultCondition" in value:
        import aws_sdk_bedrock_agent.types.missing_default_condition_flow_validation_details

        return {
            "missingDefaultCondition": aws_sdk_bedrock_agent.types.missing_default_condition_flow_validation_details.serialize_json(
                value["missingDefaultCondition"]
            )
        }
    elif "missingEndingNodes" in value:
        import aws_sdk_bedrock_agent.types.missing_ending_nodes_flow_validation_details

        return {
            "missingEndingNodes": aws_sdk_bedrock_agent.types.missing_ending_nodes_flow_validation_details.serialize_json(
                value["missingEndingNodes"]
            )
        }
    elif "missingNodeConfiguration" in value:
        import aws_sdk_bedrock_agent.types.missing_node_configuration_flow_validation_details

        return {
            "missingNodeConfiguration": aws_sdk_bedrock_agent.types.missing_node_configuration_flow_validation_details.serialize_json(
                value["missingNodeConfiguration"]
            )
        }
    elif "missingNodeInput" in value:
        import aws_sdk_bedrock_agent.types.missing_node_input_flow_validation_details

        return {
            "missingNodeInput": aws_sdk_bedrock_agent.types.missing_node_input_flow_validation_details.serialize_json(
                value["missingNodeInput"]
            )
        }
    elif "missingNodeOutput" in value:
        import aws_sdk_bedrock_agent.types.missing_node_output_flow_validation_details

        return {
            "missingNodeOutput": aws_sdk_bedrock_agent.types.missing_node_output_flow_validation_details.serialize_json(
                value["missingNodeOutput"]
            )
        }
    elif "missingStartingNodes" in value:
        import aws_sdk_bedrock_agent.types.missing_starting_nodes_flow_validation_details

        return {
            "missingStartingNodes": aws_sdk_bedrock_agent.types.missing_starting_nodes_flow_validation_details.serialize_json(
                value["missingStartingNodes"]
            )
        }
    elif "multipleNodeInputConnections" in value:
        import aws_sdk_bedrock_agent.types.multiple_node_input_connections_flow_validation_details

        return {
            "multipleNodeInputConnections": aws_sdk_bedrock_agent.types.multiple_node_input_connections_flow_validation_details.serialize_json(
                value["multipleNodeInputConnections"]
            )
        }
    elif "unfulfilledNodeInput" in value:
        import aws_sdk_bedrock_agent.types.unfulfilled_node_input_flow_validation_details

        return {
            "unfulfilledNodeInput": aws_sdk_bedrock_agent.types.unfulfilled_node_input_flow_validation_details.serialize_json(
                value["unfulfilledNodeInput"]
            )
        }
    elif "unsatisfiedConnectionConditions" in value:
        import aws_sdk_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details

        return {
            "unsatisfiedConnectionConditions": aws_sdk_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details.serialize_json(
                value["unsatisfiedConnectionConditions"]
            )
        }
    elif "unspecified" in value:
        import aws_sdk_bedrock_agent.types.unspecified_flow_validation_details

        return {
            "unspecified": aws_sdk_bedrock_agent.types.unspecified_flow_validation_details.serialize_json(
                value["unspecified"]
            )
        }
    elif "unknownNodeInput" in value:
        import aws_sdk_bedrock_agent.types.unknown_node_input_flow_validation_details

        return {
            "unknownNodeInput": aws_sdk_bedrock_agent.types.unknown_node_input_flow_validation_details.serialize_json(
                value["unknownNodeInput"]
            )
        }
    elif "unknownNodeOutput" in value:
        import aws_sdk_bedrock_agent.types.unknown_node_output_flow_validation_details

        return {
            "unknownNodeOutput": aws_sdk_bedrock_agent.types.unknown_node_output_flow_validation_details.serialize_json(
                value["unknownNodeOutput"]
            )
        }
    elif "missingLoopInputNode" in value:
        import aws_sdk_bedrock_agent.types.missing_loop_input_node_flow_validation_details

        return {
            "missingLoopInputNode": aws_sdk_bedrock_agent.types.missing_loop_input_node_flow_validation_details.serialize_json(
                value["missingLoopInputNode"]
            )
        }
    elif "missingLoopControllerNode" in value:
        import aws_sdk_bedrock_agent.types.missing_loop_controller_node_flow_validation_details

        return {
            "missingLoopControllerNode": aws_sdk_bedrock_agent.types.missing_loop_controller_node_flow_validation_details.serialize_json(
                value["missingLoopControllerNode"]
            )
        }
    elif "multipleLoopInputNodes" in value:
        import aws_sdk_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details

        return {
            "multipleLoopInputNodes": aws_sdk_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details.serialize_json(
                value["multipleLoopInputNodes"]
            )
        }
    elif "multipleLoopControllerNodes" in value:
        import aws_sdk_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details

        return {
            "multipleLoopControllerNodes": aws_sdk_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details.serialize_json(
                value["multipleLoopControllerNodes"]
            )
        }
    elif "loopIncompatibleNodeType" in value:
        import aws_sdk_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details

        return {
            "loopIncompatibleNodeType": aws_sdk_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details.serialize_json(
                value["loopIncompatibleNodeType"]
            )
        }
    elif "invalidLoopBoundary" in value:
        import aws_sdk_bedrock_agent.types.invalid_loop_boundary_flow_validation_details

        return {
            "invalidLoopBoundary": aws_sdk_bedrock_agent.types.invalid_loop_boundary_flow_validation_details.serialize_json(
                value["invalidLoopBoundary"]
            )
        }
    else:
        raise SerializationError("FlowValidationDetails: no variant present")


def deserialize_json(data: dict) -> FlowValidationDetails:
    if "cyclicConnection" in data:
        import aws_sdk_bedrock_agent.types.cyclic_connection_flow_validation_details

        return {
            "cyclicConnection": aws_sdk_bedrock_agent.types.cyclic_connection_flow_validation_details.deserialize_json(
                data["cyclicConnection"]
            )
        }
    elif "duplicateConnections" in data:
        import aws_sdk_bedrock_agent.types.duplicate_connections_flow_validation_details

        return {
            "duplicateConnections": aws_sdk_bedrock_agent.types.duplicate_connections_flow_validation_details.deserialize_json(
                data["duplicateConnections"]
            )
        }
    elif "duplicateConditionExpression" in data:
        import aws_sdk_bedrock_agent.types.duplicate_condition_expression_flow_validation_details

        return {
            "duplicateConditionExpression": aws_sdk_bedrock_agent.types.duplicate_condition_expression_flow_validation_details.deserialize_json(
                data["duplicateConditionExpression"]
            )
        }
    elif "unreachableNode" in data:
        import aws_sdk_bedrock_agent.types.unreachable_node_flow_validation_details

        return {
            "unreachableNode": aws_sdk_bedrock_agent.types.unreachable_node_flow_validation_details.deserialize_json(
                data["unreachableNode"]
            )
        }
    elif "unknownConnectionSource" in data:
        import aws_sdk_bedrock_agent.types.unknown_connection_source_flow_validation_details

        return {
            "unknownConnectionSource": aws_sdk_bedrock_agent.types.unknown_connection_source_flow_validation_details.deserialize_json(
                data["unknownConnectionSource"]
            )
        }
    elif "unknownConnectionSourceOutput" in data:
        import aws_sdk_bedrock_agent.types.unknown_connection_source_output_flow_validation_details

        return {
            "unknownConnectionSourceOutput": aws_sdk_bedrock_agent.types.unknown_connection_source_output_flow_validation_details.deserialize_json(
                data["unknownConnectionSourceOutput"]
            )
        }
    elif "unknownConnectionTarget" in data:
        import aws_sdk_bedrock_agent.types.unknown_connection_target_flow_validation_details

        return {
            "unknownConnectionTarget": aws_sdk_bedrock_agent.types.unknown_connection_target_flow_validation_details.deserialize_json(
                data["unknownConnectionTarget"]
            )
        }
    elif "unknownConnectionTargetInput" in data:
        import aws_sdk_bedrock_agent.types.unknown_connection_target_input_flow_validation_details

        return {
            "unknownConnectionTargetInput": aws_sdk_bedrock_agent.types.unknown_connection_target_input_flow_validation_details.deserialize_json(
                data["unknownConnectionTargetInput"]
            )
        }
    elif "unknownConnectionCondition" in data:
        import aws_sdk_bedrock_agent.types.unknown_connection_condition_flow_validation_details

        return {
            "unknownConnectionCondition": aws_sdk_bedrock_agent.types.unknown_connection_condition_flow_validation_details.deserialize_json(
                data["unknownConnectionCondition"]
            )
        }
    elif "malformedConditionExpression" in data:
        import aws_sdk_bedrock_agent.types.malformed_condition_expression_flow_validation_details

        return {
            "malformedConditionExpression": aws_sdk_bedrock_agent.types.malformed_condition_expression_flow_validation_details.deserialize_json(
                data["malformedConditionExpression"]
            )
        }
    elif "malformedNodeInputExpression" in data:
        import aws_sdk_bedrock_agent.types.malformed_node_input_expression_flow_validation_details

        return {
            "malformedNodeInputExpression": aws_sdk_bedrock_agent.types.malformed_node_input_expression_flow_validation_details.deserialize_json(
                data["malformedNodeInputExpression"]
            )
        }
    elif "mismatchedNodeInputType" in data:
        import aws_sdk_bedrock_agent.types.mismatched_node_input_type_flow_validation_details

        return {
            "mismatchedNodeInputType": aws_sdk_bedrock_agent.types.mismatched_node_input_type_flow_validation_details.deserialize_json(
                data["mismatchedNodeInputType"]
            )
        }
    elif "mismatchedNodeOutputType" in data:
        import aws_sdk_bedrock_agent.types.mismatched_node_output_type_flow_validation_details

        return {
            "mismatchedNodeOutputType": aws_sdk_bedrock_agent.types.mismatched_node_output_type_flow_validation_details.deserialize_json(
                data["mismatchedNodeOutputType"]
            )
        }
    elif "incompatibleConnectionDataType" in data:
        import aws_sdk_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details

        return {
            "incompatibleConnectionDataType": aws_sdk_bedrock_agent.types.incompatible_connection_data_type_flow_validation_details.deserialize_json(
                data["incompatibleConnectionDataType"]
            )
        }
    elif "missingConnectionConfiguration" in data:
        import aws_sdk_bedrock_agent.types.missing_connection_configuration_flow_validation_details

        return {
            "missingConnectionConfiguration": aws_sdk_bedrock_agent.types.missing_connection_configuration_flow_validation_details.deserialize_json(
                data["missingConnectionConfiguration"]
            )
        }
    elif "missingDefaultCondition" in data:
        import aws_sdk_bedrock_agent.types.missing_default_condition_flow_validation_details

        return {
            "missingDefaultCondition": aws_sdk_bedrock_agent.types.missing_default_condition_flow_validation_details.deserialize_json(
                data["missingDefaultCondition"]
            )
        }
    elif "missingEndingNodes" in data:
        import aws_sdk_bedrock_agent.types.missing_ending_nodes_flow_validation_details

        return {
            "missingEndingNodes": aws_sdk_bedrock_agent.types.missing_ending_nodes_flow_validation_details.deserialize_json(
                data["missingEndingNodes"]
            )
        }
    elif "missingNodeConfiguration" in data:
        import aws_sdk_bedrock_agent.types.missing_node_configuration_flow_validation_details

        return {
            "missingNodeConfiguration": aws_sdk_bedrock_agent.types.missing_node_configuration_flow_validation_details.deserialize_json(
                data["missingNodeConfiguration"]
            )
        }
    elif "missingNodeInput" in data:
        import aws_sdk_bedrock_agent.types.missing_node_input_flow_validation_details

        return {
            "missingNodeInput": aws_sdk_bedrock_agent.types.missing_node_input_flow_validation_details.deserialize_json(
                data["missingNodeInput"]
            )
        }
    elif "missingNodeOutput" in data:
        import aws_sdk_bedrock_agent.types.missing_node_output_flow_validation_details

        return {
            "missingNodeOutput": aws_sdk_bedrock_agent.types.missing_node_output_flow_validation_details.deserialize_json(
                data["missingNodeOutput"]
            )
        }
    elif "missingStartingNodes" in data:
        import aws_sdk_bedrock_agent.types.missing_starting_nodes_flow_validation_details

        return {
            "missingStartingNodes": aws_sdk_bedrock_agent.types.missing_starting_nodes_flow_validation_details.deserialize_json(
                data["missingStartingNodes"]
            )
        }
    elif "multipleNodeInputConnections" in data:
        import aws_sdk_bedrock_agent.types.multiple_node_input_connections_flow_validation_details

        return {
            "multipleNodeInputConnections": aws_sdk_bedrock_agent.types.multiple_node_input_connections_flow_validation_details.deserialize_json(
                data["multipleNodeInputConnections"]
            )
        }
    elif "unfulfilledNodeInput" in data:
        import aws_sdk_bedrock_agent.types.unfulfilled_node_input_flow_validation_details

        return {
            "unfulfilledNodeInput": aws_sdk_bedrock_agent.types.unfulfilled_node_input_flow_validation_details.deserialize_json(
                data["unfulfilledNodeInput"]
            )
        }
    elif "unsatisfiedConnectionConditions" in data:
        import aws_sdk_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details

        return {
            "unsatisfiedConnectionConditions": aws_sdk_bedrock_agent.types.unsatisfied_connection_conditions_flow_validation_details.deserialize_json(
                data["unsatisfiedConnectionConditions"]
            )
        }
    elif "unspecified" in data:
        import aws_sdk_bedrock_agent.types.unspecified_flow_validation_details

        return {
            "unspecified": aws_sdk_bedrock_agent.types.unspecified_flow_validation_details.deserialize_json(
                data["unspecified"]
            )
        }
    elif "unknownNodeInput" in data:
        import aws_sdk_bedrock_agent.types.unknown_node_input_flow_validation_details

        return {
            "unknownNodeInput": aws_sdk_bedrock_agent.types.unknown_node_input_flow_validation_details.deserialize_json(
                data["unknownNodeInput"]
            )
        }
    elif "unknownNodeOutput" in data:
        import aws_sdk_bedrock_agent.types.unknown_node_output_flow_validation_details

        return {
            "unknownNodeOutput": aws_sdk_bedrock_agent.types.unknown_node_output_flow_validation_details.deserialize_json(
                data["unknownNodeOutput"]
            )
        }
    elif "missingLoopInputNode" in data:
        import aws_sdk_bedrock_agent.types.missing_loop_input_node_flow_validation_details

        return {
            "missingLoopInputNode": aws_sdk_bedrock_agent.types.missing_loop_input_node_flow_validation_details.deserialize_json(
                data["missingLoopInputNode"]
            )
        }
    elif "missingLoopControllerNode" in data:
        import aws_sdk_bedrock_agent.types.missing_loop_controller_node_flow_validation_details

        return {
            "missingLoopControllerNode": aws_sdk_bedrock_agent.types.missing_loop_controller_node_flow_validation_details.deserialize_json(
                data["missingLoopControllerNode"]
            )
        }
    elif "multipleLoopInputNodes" in data:
        import aws_sdk_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details

        return {
            "multipleLoopInputNodes": aws_sdk_bedrock_agent.types.multiple_loop_input_nodes_flow_validation_details.deserialize_json(
                data["multipleLoopInputNodes"]
            )
        }
    elif "multipleLoopControllerNodes" in data:
        import aws_sdk_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details

        return {
            "multipleLoopControllerNodes": aws_sdk_bedrock_agent.types.multiple_loop_controller_nodes_flow_validation_details.deserialize_json(
                data["multipleLoopControllerNodes"]
            )
        }
    elif "loopIncompatibleNodeType" in data:
        import aws_sdk_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details

        return {
            "loopIncompatibleNodeType": aws_sdk_bedrock_agent.types.loop_incompatible_node_type_flow_validation_details.deserialize_json(
                data["loopIncompatibleNodeType"]
            )
        }
    elif "invalidLoopBoundary" in data:
        import aws_sdk_bedrock_agent.types.invalid_loop_boundary_flow_validation_details

        return {
            "invalidLoopBoundary": aws_sdk_bedrock_agent.types.invalid_loop_boundary_flow_validation_details.deserialize_json(
                data["invalidLoopBoundary"]
            )
        }
    else:
        raise DeserializationError("FlowValidationDetails: no recognized variant key")
