"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowRuleDefinitionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.id_mapping_workflow_rule_definition_type

IdMappingWorkflowRuleDefinitionTypeList: TypeAlias = list[
    "capo_entityresolution.types.id_mapping_workflow_rule_definition_type.IdMappingWorkflowRuleDefinitionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowRuleDefinitionTypeList) -> list:
    import capo_entityresolution.types.id_mapping_workflow_rule_definition_type

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.id_mapping_workflow_rule_definition_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdMappingWorkflowRuleDefinitionTypeList:
    import capo_entityresolution.types.id_mapping_workflow_rule_definition_type

    out: IdMappingWorkflowRuleDefinitionTypeList = []
    for item in data:
        out.append(
            capo_entityresolution.types.id_mapping_workflow_rule_definition_type.deserialize_json(
                item
            )
        )
    return out
