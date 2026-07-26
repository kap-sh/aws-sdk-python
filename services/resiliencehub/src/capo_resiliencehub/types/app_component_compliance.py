"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppComponentCompliance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.assessment_compliance
    import capo_resiliencehub.types.compliance_status
    import capo_resiliencehub.types.cost
    import capo_resiliencehub.types.entity_id
    import capo_resiliencehub.types.resiliency_score
    import capo_resiliencehub.types.string500


class AppComponentCompliance(TypedDict, closed=True):
    cost: NotRequired["capo_resiliencehub.types.cost.Cost"]
    """<p>The cost for the application.</p>"""
    app_component_name: NotRequired["capo_resiliencehub.types.entity_id.EntityId"]
    """<p>Name of the Application Component.</p>"""
    compliance: NotRequired[
        "capo_resiliencehub.types.assessment_compliance.AssessmentCompliance"
    ]
    """<p>The compliance of the Application Component against the resiliency policy.</p>"""
    message: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>The compliance message.</p>"""
    status: NotRequired["capo_resiliencehub.types.compliance_status.ComplianceStatus"]
    """<p>Status of the action.</p>"""
    resiliency_score: NotRequired[
        "capo_resiliencehub.types.resiliency_score.ResiliencyScore"
    ]
    """<p>The current resiliency score for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppComponentCompliance) -> dict:
    out: dict = {}
    if "cost" in value:
        import capo_resiliencehub.types.cost

        out["cost"] = capo_resiliencehub.types.cost.serialize_json(value["cost"])
    if "app_component_name" in value:
        out["appComponentName"] = value["app_component_name"]
    if "compliance" in value:
        import capo_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            capo_resiliencehub.types.assessment_compliance.serialize_json(
                value["compliance"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    if "status" in value:
        import capo_resiliencehub.types.compliance_status

        out["status"] = capo_resiliencehub.types.compliance_status.serialize_json(
            value["status"]
        )
    if "resiliency_score" in value:
        import capo_resiliencehub.types.resiliency_score

        out["resiliencyScore"] = (
            capo_resiliencehub.types.resiliency_score.serialize_json(
                value["resiliency_score"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppComponentCompliance:
    out: AppComponentCompliance = {}  # type: ignore[typeddict-item]
    if "cost" in data:
        import capo_resiliencehub.types.cost

        out["cost"] = capo_resiliencehub.types.cost.deserialize_json(data["cost"])
    if "appComponentName" in data:
        out["app_component_name"] = data["appComponentName"]
    if "compliance" in data:
        import capo_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            capo_resiliencehub.types.assessment_compliance.deserialize_json(
                data["compliance"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    if "status" in data:
        import capo_resiliencehub.types.compliance_status

        out["status"] = capo_resiliencehub.types.compliance_status.deserialize_json(
            data["status"]
        )
    if "resiliencyScore" in data:
        import capo_resiliencehub.types.resiliency_score

        out["resiliency_score"] = (
            capo_resiliencehub.types.resiliency_score.deserialize_json(
                data["resiliencyScore"]
            )
        )
    return out
