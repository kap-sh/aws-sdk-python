"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ComplianceDrift``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.assessment_compliance
    import aws_sdk_resiliencehub.types.difference_type
    import aws_sdk_resiliencehub.types.drift_type
    import aws_sdk_resiliencehub.types.string255


class ComplianceDrift(TypedDict, closed=True):
    entity_id: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Identifier of an entity in which drift was detected. For compliance drift, the entity ID can be either application ID or the AppComponent ID.</p>"""
    entity_type: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>The type of entity in which drift was detected. For compliance drifts, Resilience Hub supports <code>AWS::ResilienceHub::AppComponent</code> and <code>AWS::ResilienceHub::Application</code>.</p>"""
    drift_type: NotRequired["aws_sdk_resiliencehub.types.drift_type.DriftType"]
    """<p>The type of drift detected. Currently, Resilience Hub supports only <b>ApplicationCompliance</b> drift type.</p>"""
    app_id: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Identifier of your application.</p>"""
    app_version: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Published version of your application on which drift was detected.</p>"""
    expected_reference_id: NotRequired[
        "aws_sdk_resiliencehub.types.string255.String255"
    ]
    """<p>Assessment identifier of a previous assessment of the same application version. Resilience Hub uses the previous assessment (associated with the reference identifier) to compare the compliance with the current assessment to identify drifts.</p>"""
    expected_value: NotRequired[
        "aws_sdk_resiliencehub.types.assessment_compliance.AssessmentCompliance"
    ]
    """<p>The expected compliance value of an entity.</p>"""
    actual_reference_id: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Assessment identifier that is associated with this drift item.</p>"""
    actual_value: NotRequired[
        "aws_sdk_resiliencehub.types.assessment_compliance.AssessmentCompliance"
    ]
    """<p>Actual compliance value of the entity.</p>"""
    diff_type: NotRequired["aws_sdk_resiliencehub.types.difference_type.DifferenceType"]
    """<p>Difference type between actual and expected recovery point objective (RPO) and recovery time objective (RTO) values. Currently, Resilience Hub supports only <code>NotEqual</code> difference type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComplianceDrift) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_type" in value:
        out["entityType"] = value["entity_type"]
    if "drift_type" in value:
        import aws_sdk_resiliencehub.types.drift_type

        out["driftType"] = aws_sdk_resiliencehub.types.drift_type.serialize_json(
            value["drift_type"]
        )
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    if "expected_reference_id" in value:
        out["expectedReferenceId"] = value["expected_reference_id"]
    if "expected_value" in value:
        import aws_sdk_resiliencehub.types.assessment_compliance

        out["expectedValue"] = (
            aws_sdk_resiliencehub.types.assessment_compliance.serialize_json(
                value["expected_value"]
            )
        )
    if "actual_reference_id" in value:
        out["actualReferenceId"] = value["actual_reference_id"]
    if "actual_value" in value:
        import aws_sdk_resiliencehub.types.assessment_compliance

        out["actualValue"] = (
            aws_sdk_resiliencehub.types.assessment_compliance.serialize_json(
                value["actual_value"]
            )
        )
    if "diff_type" in value:
        import aws_sdk_resiliencehub.types.difference_type

        out["diffType"] = aws_sdk_resiliencehub.types.difference_type.serialize_json(
            value["diff_type"]
        )
    return out


def deserialize_json(data: dict) -> ComplianceDrift:
    out: ComplianceDrift = {}  # type: ignore[typeddict-item]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "entityType" in data:
        out["entity_type"] = data["entityType"]
    if "driftType" in data:
        import aws_sdk_resiliencehub.types.drift_type

        out["drift_type"] = aws_sdk_resiliencehub.types.drift_type.deserialize_json(
            data["driftType"]
        )
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    if "expectedReferenceId" in data:
        out["expected_reference_id"] = data["expectedReferenceId"]
    if "expectedValue" in data:
        import aws_sdk_resiliencehub.types.assessment_compliance

        out["expected_value"] = (
            aws_sdk_resiliencehub.types.assessment_compliance.deserialize_json(
                data["expectedValue"]
            )
        )
    if "actualReferenceId" in data:
        out["actual_reference_id"] = data["actualReferenceId"]
    if "actualValue" in data:
        import aws_sdk_resiliencehub.types.assessment_compliance

        out["actual_value"] = (
            aws_sdk_resiliencehub.types.assessment_compliance.deserialize_json(
                data["actualValue"]
            )
        )
    if "diffType" in data:
        import aws_sdk_resiliencehub.types.difference_type

        out["diff_type"] = aws_sdk_resiliencehub.types.difference_type.deserialize_json(
            data["diffType"]
        )
    return out
