"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ComponentRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.config_recommendation_list
    import aws_sdk_resiliencehub.types.entity_id
    import aws_sdk_resiliencehub.types.recommendation_compliance_status


class ComponentRecommendation(TypedDict, closed=True):
    app_component_name: "aws_sdk_resiliencehub.types.entity_id.EntityId"
    """<p>Name of the Application Component.</p>"""
    recommendation_status: "aws_sdk_resiliencehub.types.recommendation_compliance_status.RecommendationComplianceStatus"
    """<p>Status of the recommendation.</p>"""
    config_recommendations: "aws_sdk_resiliencehub.types.config_recommendation_list.ConfigRecommendationList"
    """<p>List of recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentRecommendation) -> dict:
    out: dict = {}
    out["appComponentName"] = value["app_component_name"]
    import aws_sdk_resiliencehub.types.recommendation_compliance_status

    out["recommendationStatus"] = (
        aws_sdk_resiliencehub.types.recommendation_compliance_status.serialize_json(
            value["recommendation_status"]
        )
    )
    import aws_sdk_resiliencehub.types.config_recommendation_list

    out["configRecommendations"] = (
        aws_sdk_resiliencehub.types.config_recommendation_list.serialize_json(
            value["config_recommendations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ComponentRecommendation:
    out: ComponentRecommendation = {}  # type: ignore[typeddict-item]
    if "appComponentName" in data:
        out["app_component_name"] = data["appComponentName"]
    else:
        raise DeserializationError(
            "ComponentRecommendation.app_component_name required"
        )
    if "recommendationStatus" in data:
        import aws_sdk_resiliencehub.types.recommendation_compliance_status

        out["recommendation_status"] = (
            aws_sdk_resiliencehub.types.recommendation_compliance_status.deserialize_json(
                data["recommendationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ComponentRecommendation.recommendation_status required"
        )
    if "configRecommendations" in data:
        import aws_sdk_resiliencehub.types.config_recommendation_list

        out["config_recommendations"] = (
            aws_sdk_resiliencehub.types.config_recommendation_list.deserialize_json(
                data["configRecommendations"]
            )
        )
    else:
        raise DeserializationError(
            "ComponentRecommendation.config_recommendations required"
        )
    return out
