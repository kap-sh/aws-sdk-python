"""Generated from Smithy shape ``com.amazonaws.entityresolution#NamespaceRuleBasedProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.attribute_matching_model
    import capo_entityresolution.types.id_mapping_workflow_rule_definition_type_list
    import capo_entityresolution.types.record_matching_model_list
    import capo_entityresolution.types.rule_list


class NamespaceRuleBasedProperties(TypedDict, closed=True):
    rules: NotRequired["capo_entityresolution.types.rule_list.RuleList"]
    """<p> The rules for the ID namespace.</p>"""
    rule_definition_types: NotRequired[
        "capo_entityresolution.types.id_mapping_workflow_rule_definition_type_list.IdMappingWorkflowRuleDefinitionTypeList"
    ]
    """<p> The sets of rules you can use in an ID mapping workflow. The limitations specified for the source and target must be compatible.</p>"""
    attribute_matching_model: NotRequired[
        "capo_entityresolution.types.attribute_matching_model.AttributeMatchingModel"
    ]
    """<p>The comparison type. You can either choose <code>ONE_TO_ONE</code> or <code>MANY_TO_MANY</code> as the <code>attributeMatchingModel</code>. </p> <p>If you choose <code>ONE_TO_ONE</code>, the system can only match attributes if the sub-types are an exact match. For example, for the <code>Email</code> attribute type, the system will only consider it a match if the value of the <code>Email</code> field of Profile A matches the value of the <code>Email</code> field of Profile B.</p> <p>If you choose <code>MANY_TO_MANY</code>, the system can match attributes across the sub-types of an attribute type. For example, if the value of the <code>Email</code> field of Profile A matches the value of <code>BusinessEmail</code> field of Profile B, the two profiles are matched on the <code>Email</code> attribute type. </p>"""
    record_matching_models: NotRequired[
        "capo_entityresolution.types.record_matching_model_list.RecordMatchingModelList"
    ]
    """<p> The type of matching record that is allowed to be used in an ID mapping workflow. </p> <p>If the value is set to <code>ONE_SOURCE_TO_ONE_TARGET</code>, only one record in the source is matched to one record in the target. </p> <p>If the value is set to <code>MANY_SOURCE_TO_ONE_TARGET</code>, all matching records in the source are matched to one record in the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceRuleBasedProperties) -> dict:
    out: dict = {}
    if "rules" in value:
        import capo_entityresolution.types.rule_list

        out["rules"] = capo_entityresolution.types.rule_list.serialize_json(
            value["rules"]
        )
    if "rule_definition_types" in value:
        import capo_entityresolution.types.id_mapping_workflow_rule_definition_type_list

        out["ruleDefinitionTypes"] = (
            capo_entityresolution.types.id_mapping_workflow_rule_definition_type_list.serialize_json(
                value["rule_definition_types"]
            )
        )
    if "attribute_matching_model" in value:
        import capo_entityresolution.types.attribute_matching_model

        out["attributeMatchingModel"] = (
            capo_entityresolution.types.attribute_matching_model.serialize_json(
                value["attribute_matching_model"]
            )
        )
    if "record_matching_models" in value:
        import capo_entityresolution.types.record_matching_model_list

        out["recordMatchingModels"] = (
            capo_entityresolution.types.record_matching_model_list.serialize_json(
                value["record_matching_models"]
            )
        )
    return out


def deserialize_json(data: dict) -> NamespaceRuleBasedProperties:
    out: NamespaceRuleBasedProperties = {}  # type: ignore[typeddict-item]
    if "rules" in data:
        import capo_entityresolution.types.rule_list

        out["rules"] = capo_entityresolution.types.rule_list.deserialize_json(
            data["rules"]
        )
    if "ruleDefinitionTypes" in data:
        import capo_entityresolution.types.id_mapping_workflow_rule_definition_type_list

        out["rule_definition_types"] = (
            capo_entityresolution.types.id_mapping_workflow_rule_definition_type_list.deserialize_json(
                data["ruleDefinitionTypes"]
            )
        )
    if "attributeMatchingModel" in data:
        import capo_entityresolution.types.attribute_matching_model

        out["attribute_matching_model"] = (
            capo_entityresolution.types.attribute_matching_model.deserialize_json(
                data["attributeMatchingModel"]
            )
        )
    if "recordMatchingModels" in data:
        import capo_entityresolution.types.record_matching_model_list

        out["record_matching_models"] = (
            capo_entityresolution.types.record_matching_model_list.deserialize_json(
                data["recordMatchingModels"]
            )
        )
    return out
