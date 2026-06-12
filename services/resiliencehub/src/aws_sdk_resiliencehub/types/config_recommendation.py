"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ConfigRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.assessment_compliance
    import aws_sdk_resiliencehub.types.config_recommendation_optimization_type
    import aws_sdk_resiliencehub.types.cost
    import aws_sdk_resiliencehub.types.entity_description
    import aws_sdk_resiliencehub.types.entity_id
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.ha_architecture
    import aws_sdk_resiliencehub.types.recommendation_compliance
    import aws_sdk_resiliencehub.types.spec_reference_id
    import aws_sdk_resiliencehub.types.suggested_changes_list


class ConfigRecommendation(TypedDict):
    cost: NotRequired["aws_sdk_resiliencehub.types.cost.Cost"]
    """<p>The cost for the application.</p>"""
    app_component_name: NotRequired["aws_sdk_resiliencehub.types.entity_id.EntityId"]
    """<p>Name of the Application Component.</p>"""
    compliance: NotRequired[
        "aws_sdk_resiliencehub.types.assessment_compliance.AssessmentCompliance"
    ]
    """<p>The current compliance against the resiliency policy before applying the configuration change.</p>"""
    recommendation_compliance: NotRequired[
        "aws_sdk_resiliencehub.types.recommendation_compliance.RecommendationCompliance"
    ]
    """<p>The expected compliance against the resiliency policy after applying the configuration change.</p>"""
    optimization_type: "aws_sdk_resiliencehub.types.config_recommendation_optimization_type.ConfigRecommendationOptimizationType"
    """<p>The type of optimization.</p>"""
    name: "aws_sdk_resiliencehub.types.entity_name.EntityName"
    """<p>The name of the recommendation configuration.</p>"""
    description: NotRequired[
        "aws_sdk_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>The optional description for an app.</p>"""
    suggested_changes: NotRequired[
        "aws_sdk_resiliencehub.types.suggested_changes_list.SuggestedChangesList"
    ]
    """<p>List of the suggested configuration changes.</p>"""
    ha_architecture: NotRequired[
        "aws_sdk_resiliencehub.types.ha_architecture.HaArchitecture"
    ]
    """<p>The architecture type.</p>"""
    reference_id: "aws_sdk_resiliencehub.types.spec_reference_id.SpecReferenceId"
    """<p>Reference identifier for the recommendation configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigRecommendation) -> dict:
    out: dict = {}
    if "cost" in value:
        import aws_sdk_resiliencehub.types.cost

        out["cost"] = aws_sdk_resiliencehub.types.cost.serialize_json(value["cost"])
    if "app_component_name" in value:
        out["appComponentName"] = value["app_component_name"]
    if "compliance" in value:
        import aws_sdk_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            aws_sdk_resiliencehub.types.assessment_compliance.serialize_json(
                value["compliance"]
            )
        )
    if "recommendation_compliance" in value:
        import aws_sdk_resiliencehub.types.recommendation_compliance

        out["recommendationCompliance"] = (
            aws_sdk_resiliencehub.types.recommendation_compliance.serialize_json(
                value["recommendation_compliance"]
            )
        )
    import aws_sdk_resiliencehub.types.config_recommendation_optimization_type

    out["optimizationType"] = (
        aws_sdk_resiliencehub.types.config_recommendation_optimization_type.serialize_json(
            value["optimization_type"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "suggested_changes" in value:
        import aws_sdk_resiliencehub.types.suggested_changes_list

        out["suggestedChanges"] = (
            aws_sdk_resiliencehub.types.suggested_changes_list.serialize_json(
                value["suggested_changes"]
            )
        )
    if "ha_architecture" in value:
        import aws_sdk_resiliencehub.types.ha_architecture

        out["haArchitecture"] = (
            aws_sdk_resiliencehub.types.ha_architecture.serialize_json(
                value["ha_architecture"]
            )
        )
    out["referenceId"] = value["reference_id"]
    return out


def deserialize_json(data: dict) -> ConfigRecommendation:
    out: ConfigRecommendation = {}  # type: ignore[typeddict-item]
    if "cost" in data:
        import aws_sdk_resiliencehub.types.cost

        out["cost"] = aws_sdk_resiliencehub.types.cost.deserialize_json(data["cost"])
    if "appComponentName" in data:
        out["app_component_name"] = data["appComponentName"]
    if "compliance" in data:
        import aws_sdk_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            aws_sdk_resiliencehub.types.assessment_compliance.deserialize_json(
                data["compliance"]
            )
        )
    if "recommendationCompliance" in data:
        import aws_sdk_resiliencehub.types.recommendation_compliance

        out["recommendation_compliance"] = (
            aws_sdk_resiliencehub.types.recommendation_compliance.deserialize_json(
                data["recommendationCompliance"]
            )
        )
    if "optimizationType" in data:
        import aws_sdk_resiliencehub.types.config_recommendation_optimization_type

        out["optimization_type"] = (
            aws_sdk_resiliencehub.types.config_recommendation_optimization_type.deserialize_json(
                data["optimizationType"]
            )
        )
    else:
        raise DeserializationError("ConfigRecommendation.optimization_type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfigRecommendation.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "suggestedChanges" in data:
        import aws_sdk_resiliencehub.types.suggested_changes_list

        out["suggested_changes"] = (
            aws_sdk_resiliencehub.types.suggested_changes_list.deserialize_json(
                data["suggestedChanges"]
            )
        )
    if "haArchitecture" in data:
        import aws_sdk_resiliencehub.types.ha_architecture

        out["ha_architecture"] = (
            aws_sdk_resiliencehub.types.ha_architecture.deserialize_json(
                data["haArchitecture"]
            )
        )
    if "referenceId" in data:
        out["reference_id"] = data["referenceId"]
    else:
        raise DeserializationError("ConfigRecommendation.reference_id required")
    return out
