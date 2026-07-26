"""Generated from Smithy shape ``com.amazonaws.resiliencehub#SopRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.document_name
    import capo_resiliencehub.types.entity_id
    import capo_resiliencehub.types.recommendation_item_list
    import capo_resiliencehub.types.recommendation_status
    import capo_resiliencehub.types.sop_service_type
    import capo_resiliencehub.types.spec_reference_id
    import capo_resiliencehub.types.string500
    import capo_resiliencehub.types.uuid


class SopRecommendation(TypedDict, closed=True):
    service_type: "capo_resiliencehub.types.sop_service_type.SopServiceType"
    """<p>The service type.</p>"""
    app_component_name: NotRequired["capo_resiliencehub.types.entity_id.EntityId"]
    """<p>Name of the Application Component.</p>"""
    description: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Description of the SOP recommendation.</p>"""
    recommendation_id: "capo_resiliencehub.types.uuid.Uuid"
    """<p>Identifier for the SOP recommendation.</p>"""
    name: NotRequired["capo_resiliencehub.types.document_name.DocumentName"]
    """<p>Name of the SOP recommendation.</p>"""
    items: NotRequired[
        "capo_resiliencehub.types.recommendation_item_list.RecommendationItemList"
    ]
    """<p>The recommendation items.</p>"""
    reference_id: "capo_resiliencehub.types.spec_reference_id.SpecReferenceId"
    """<p>Reference identifier for the SOP recommendation.</p>"""
    prerequisite: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Prerequisite for the SOP recommendation.</p>"""
    recommendation_status: NotRequired[
        "capo_resiliencehub.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Status of the recommended standard operating procedure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SopRecommendation) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.sop_service_type

    out["serviceType"] = capo_resiliencehub.types.sop_service_type.serialize_json(
        value["service_type"]
    )
    if "app_component_name" in value:
        out["appComponentName"] = value["app_component_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["recommendationId"] = value["recommendation_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "items" in value:
        import capo_resiliencehub.types.recommendation_item_list

        out["items"] = capo_resiliencehub.types.recommendation_item_list.serialize_json(
            value["items"]
        )
    out["referenceId"] = value["reference_id"]
    if "prerequisite" in value:
        out["prerequisite"] = value["prerequisite"]
    if "recommendation_status" in value:
        import capo_resiliencehub.types.recommendation_status

        out["recommendationStatus"] = (
            capo_resiliencehub.types.recommendation_status.serialize_json(
                value["recommendation_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SopRecommendation:
    out: SopRecommendation = {}  # type: ignore[typeddict-item]
    if "serviceType" in data:
        import capo_resiliencehub.types.sop_service_type

        out["service_type"] = (
            capo_resiliencehub.types.sop_service_type.deserialize_json(
                data["serviceType"]
            )
        )
    else:
        raise DeserializationError("SopRecommendation.service_type required")
    if "appComponentName" in data:
        out["app_component_name"] = data["appComponentName"]
    if "description" in data:
        out["description"] = data["description"]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    else:
        raise DeserializationError("SopRecommendation.recommendation_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "items" in data:
        import capo_resiliencehub.types.recommendation_item_list

        out["items"] = (
            capo_resiliencehub.types.recommendation_item_list.deserialize_json(
                data["items"]
            )
        )
    if "referenceId" in data:
        out["reference_id"] = data["referenceId"]
    else:
        raise DeserializationError("SopRecommendation.reference_id required")
    if "prerequisite" in data:
        out["prerequisite"] = data["prerequisite"]
    if "recommendationStatus" in data:
        import capo_resiliencehub.types.recommendation_status

        out["recommendation_status"] = (
            capo_resiliencehub.types.recommendation_status.deserialize_json(
                data["recommendationStatus"]
            )
        )
    return out
