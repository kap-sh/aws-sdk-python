"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowRuleDefinitionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_mapping_workflow_rule_definition_type

IdMappingWorkflowRuleDefinitionTypeList: TypeAlias = list[
    "aws_sdk_entityresolution.types.id_mapping_workflow_rule_definition_type.IdMappingWorkflowRuleDefinitionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowRuleDefinitionTypeList) -> list:
    import aws_sdk_entityresolution.types.id_mapping_workflow_rule_definition_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.id_mapping_workflow_rule_definition_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdMappingWorkflowRuleDefinitionTypeList:
    import aws_sdk_entityresolution.types.id_mapping_workflow_rule_definition_type

    out: IdMappingWorkflowRuleDefinitionTypeList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.id_mapping_workflow_rule_definition_type.deserialize_json(
                item
            )
        )
    return out
