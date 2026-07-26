"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_description
    import capo_auditmanager.types.assessment_name
    import capo_auditmanager.types.assessment_reports_destination
    import capo_auditmanager.types.roles
    import capo_auditmanager.types.scope
    import capo_auditmanager.types.tag_map
    import capo_auditmanager.types.uuid


class CreateAssessmentRequest(TypedDict, closed=True):
    name: "capo_auditmanager.types.assessment_name.AssessmentName"
    """<p> The name of the assessment to be created. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.assessment_description.AssessmentDescription"
    ]
    """<p> The optional description of the assessment to be created. </p>"""
    assessment_reports_destination: "capo_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
    """<p> The assessment report storage destination for the assessment that's being created. </p>"""
    scope: "capo_auditmanager.types.scope.Scope"
    roles: "capo_auditmanager.types.roles.Roles"
    """<p> The list of roles for the assessment. </p>"""
    framework_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the framework that the assessment will be created from. </p>"""
    tags: NotRequired["capo_auditmanager.types.tag_map.TagMap"]
    """<p> The tags that are associated with the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_auditmanager.types.assessment_reports_destination

    out["assessmentReportsDestination"] = (
        capo_auditmanager.types.assessment_reports_destination.serialize_json(
            value["assessment_reports_destination"]
        )
    )
    import capo_auditmanager.types.scope

    out["scope"] = capo_auditmanager.types.scope.serialize_json(value["scope"])
    import capo_auditmanager.types.roles

    out["roles"] = capo_auditmanager.types.roles.serialize_json(value["roles"])
    out["frameworkId"] = value["framework_id"]
    if "tags" in value:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAssessmentRequest:
    out: CreateAssessmentRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssessmentRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "assessmentReportsDestination" in data:
        import capo_auditmanager.types.assessment_reports_destination

        out["assessment_reports_destination"] = (
            capo_auditmanager.types.assessment_reports_destination.deserialize_json(
                data["assessmentReportsDestination"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAssessmentRequest.assessment_reports_destination required"
        )
    if "scope" in data:
        import capo_auditmanager.types.scope

        out["scope"] = capo_auditmanager.types.scope.deserialize_json(data["scope"])
    else:
        raise DeserializationError("CreateAssessmentRequest.scope required")
    if "roles" in data:
        import capo_auditmanager.types.roles

        out["roles"] = capo_auditmanager.types.roles.deserialize_json(data["roles"])
    else:
        raise DeserializationError("CreateAssessmentRequest.roles required")
    if "frameworkId" in data:
        out["framework_id"] = data["frameworkId"]
    else:
        raise DeserializationError("CreateAssessmentRequest.framework_id required")
    if "tags" in data:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.deserialize_json(data["tags"])
    return out
