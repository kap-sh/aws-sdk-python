"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentFramework``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_control_sets
    import capo_auditmanager.types.audit_manager_arn
    import capo_auditmanager.types.framework_metadata
    import capo_auditmanager.types.uuid


class AssessmentFramework(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the framework. </p>"""
    arn: NotRequired["capo_auditmanager.types.audit_manager_arn.AuditManagerArn"]
    """<p> The Amazon Resource Name (ARN) of the framework. </p>"""
    metadata: NotRequired[
        "capo_auditmanager.types.framework_metadata.FrameworkMetadata"
    ]
    control_sets: NotRequired[
        "capo_auditmanager.types.assessment_control_sets.AssessmentControlSets"
    ]
    """<p> The control sets that are associated with the framework. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentFramework) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "metadata" in value:
        import capo_auditmanager.types.framework_metadata

        out["metadata"] = capo_auditmanager.types.framework_metadata.serialize_json(
            value["metadata"]
        )
    if "control_sets" in value:
        import capo_auditmanager.types.assessment_control_sets

        out["controlSets"] = (
            capo_auditmanager.types.assessment_control_sets.serialize_json(
                value["control_sets"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssessmentFramework:
    out: AssessmentFramework = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "metadata" in data:
        import capo_auditmanager.types.framework_metadata

        out["metadata"] = capo_auditmanager.types.framework_metadata.deserialize_json(
            data["metadata"]
        )
    if "controlSets" in data:
        import capo_auditmanager.types.assessment_control_sets

        out["control_sets"] = (
            capo_auditmanager.types.assessment_control_sets.deserialize_json(
                data["controlSets"]
            )
        )
    return out
