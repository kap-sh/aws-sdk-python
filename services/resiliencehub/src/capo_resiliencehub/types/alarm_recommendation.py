"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AlarmRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.alarm_type
    import capo_resiliencehub.types.app_component_name_list
    import capo_resiliencehub.types.entity_description
    import capo_resiliencehub.types.entity_id
    import capo_resiliencehub.types.recommendation_item_list
    import capo_resiliencehub.types.recommendation_status
    import capo_resiliencehub.types.spec_reference_id
    import capo_resiliencehub.types.string500
    import capo_resiliencehub.types.uuid


class AlarmRecommendation(TypedDict, closed=True):
    recommendation_id: "capo_resiliencehub.types.uuid.Uuid"
    """<p>Identifier of the alarm recommendation.</p>"""
    reference_id: "capo_resiliencehub.types.spec_reference_id.SpecReferenceId"
    """<p>Reference identifier of the alarm recommendation.</p>"""
    name: "capo_resiliencehub.types.string500.String500"
    """<p>Name of the alarm recommendation.</p>"""
    description: NotRequired[
        "capo_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>Description of the alarm recommendation.</p>"""
    type: "capo_resiliencehub.types.alarm_type.AlarmType"
    """<p>Type of alarm recommendation.</p>"""
    app_component_name: NotRequired["capo_resiliencehub.types.entity_id.EntityId"]
    """<p>Application Component name for the CloudWatch alarm recommendation. This name is saved as the first item in the <code>appComponentNames</code> list.</p>"""
    items: NotRequired[
        "capo_resiliencehub.types.recommendation_item_list.RecommendationItemList"
    ]
    """<p>List of CloudWatch alarm recommendations.</p>"""
    prerequisite: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>The prerequisite for the alarm recommendation.</p>"""
    app_component_names: NotRequired[
        "capo_resiliencehub.types.app_component_name_list.AppComponentNameList"
    ]
    """<p>List of Application Component names for the CloudWatch alarm recommendation.</p>"""
    recommendation_status: NotRequired[
        "capo_resiliencehub.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Status of the recommended Amazon CloudWatch alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmRecommendation) -> dict:
    out: dict = {}
    out["recommendationId"] = value["recommendation_id"]
    out["referenceId"] = value["reference_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_resiliencehub.types.alarm_type

    out["type"] = capo_resiliencehub.types.alarm_type.serialize_json(value["type"])
    if "app_component_name" in value:
        out["appComponentName"] = value["app_component_name"]
    if "items" in value:
        import capo_resiliencehub.types.recommendation_item_list

        out["items"] = capo_resiliencehub.types.recommendation_item_list.serialize_json(
            value["items"]
        )
    if "prerequisite" in value:
        out["prerequisite"] = value["prerequisite"]
    if "app_component_names" in value:
        import capo_resiliencehub.types.app_component_name_list

        out["appComponentNames"] = (
            capo_resiliencehub.types.app_component_name_list.serialize_json(
                value["app_component_names"]
            )
        )
    if "recommendation_status" in value:
        import capo_resiliencehub.types.recommendation_status

        out["recommendationStatus"] = (
            capo_resiliencehub.types.recommendation_status.serialize_json(
                value["recommendation_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AlarmRecommendation:
    out: AlarmRecommendation = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    else:
        raise DeserializationError("AlarmRecommendation.recommendation_id required")
    if "referenceId" in data:
        out["reference_id"] = data["referenceId"]
    else:
        raise DeserializationError("AlarmRecommendation.reference_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AlarmRecommendation.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import capo_resiliencehub.types.alarm_type

        out["type"] = capo_resiliencehub.types.alarm_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("AlarmRecommendation.type required")
    if "appComponentName" in data:
        out["app_component_name"] = data["appComponentName"]
    if "items" in data:
        import capo_resiliencehub.types.recommendation_item_list

        out["items"] = (
            capo_resiliencehub.types.recommendation_item_list.deserialize_json(
                data["items"]
            )
        )
    if "prerequisite" in data:
        out["prerequisite"] = data["prerequisite"]
    if "appComponentNames" in data:
        import capo_resiliencehub.types.app_component_name_list

        out["app_component_names"] = (
            capo_resiliencehub.types.app_component_name_list.deserialize_json(
                data["appComponentNames"]
            )
        )
    if "recommendationStatus" in data:
        import capo_resiliencehub.types.recommendation_status

        out["recommendation_status"] = (
            capo_resiliencehub.types.recommendation_status.deserialize_json(
                data["recommendationStatus"]
            )
        )
    return out
