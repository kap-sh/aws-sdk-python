"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.arn_count
    import capo_inspector.types.assessment_run_duration
    import capo_inspector.types.assessment_template_name
    import capo_inspector.types.assessment_template_rules_package_arn_list
    import capo_inspector.types.timestamp
    import capo_inspector.types.user_attribute_list


class AssessmentTemplate(TypedDict, closed=True):
    arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment template.</p>"""
    name: "capo_inspector.types.assessment_template_name.AssessmentTemplateName"
    """<p>The name of the assessment template.</p>"""
    assessment_target_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment target that corresponds to this assessment template.</p>"""
    duration_in_seconds: (
        "capo_inspector.types.assessment_run_duration.AssessmentRunDuration"
    )
    """<p>The duration in seconds specified for this assessment template. The default value is 3600 seconds (one hour). The maximum value is 86400 seconds (one day).</p>"""
    rules_package_arns: "capo_inspector.types.assessment_template_rules_package_arn_list.AssessmentTemplateRulesPackageArnList"
    """<p>The rules packages that are specified for this assessment template.</p>"""
    user_attributes_for_findings: (
        "capo_inspector.types.user_attribute_list.UserAttributeList"
    )
    """<p>The user-defined attributes that are assigned to every generated finding from the assessment run that uses this assessment template.</p>"""
    last_assessment_run_arn: NotRequired["capo_inspector.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the most recent assessment run associated with this assessment template. This value exists only when the value of assessmentRunCount is greaterpa than zero.</p>"""
    assessment_run_count: "capo_inspector.types.arn_count.ArnCount"
    """<p>The number of existing assessment runs associated with this assessment template. This value can be zero or a positive integer.</p>"""
    created_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The time at which the assessment template is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentTemplate) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["assessmentTargetArn"] = value["assessment_target_arn"]
    out["durationInSeconds"] = value["duration_in_seconds"]
    import capo_inspector.types.assessment_template_rules_package_arn_list

    out["rulesPackageArns"] = (
        capo_inspector.types.assessment_template_rules_package_arn_list.serialize_aws_json_1_1(
            value["rules_package_arns"]
        )
    )
    import capo_inspector.types.user_attribute_list

    out["userAttributesForFindings"] = (
        capo_inspector.types.user_attribute_list.serialize_aws_json_1_1(
            value["user_attributes_for_findings"]
        )
    )
    if "last_assessment_run_arn" in value:
        out["lastAssessmentRunArn"] = value["last_assessment_run_arn"]
    out["assessmentRunCount"] = value["assessment_run_count"]
    import capo_inspector.types.timestamp

    out["createdAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentTemplate:
    out: AssessmentTemplate = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AssessmentTemplate.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssessmentTemplate.name required")
    if "assessmentTargetArn" in data:
        out["assessment_target_arn"] = data["assessmentTargetArn"]
    else:
        raise DeserializationError("AssessmentTemplate.assessment_target_arn required")
    if "durationInSeconds" in data:
        out["duration_in_seconds"] = data["durationInSeconds"]
    else:
        raise DeserializationError("AssessmentTemplate.duration_in_seconds required")
    if "rulesPackageArns" in data:
        import capo_inspector.types.assessment_template_rules_package_arn_list

        out["rules_package_arns"] = (
            capo_inspector.types.assessment_template_rules_package_arn_list.deserialize_aws_json_1_1(
                data["rulesPackageArns"]
            )
        )
    else:
        raise DeserializationError("AssessmentTemplate.rules_package_arns required")
    if "userAttributesForFindings" in data:
        import capo_inspector.types.user_attribute_list

        out["user_attributes_for_findings"] = (
            capo_inspector.types.user_attribute_list.deserialize_aws_json_1_1(
                data["userAttributesForFindings"]
            )
        )
    else:
        raise DeserializationError(
            "AssessmentTemplate.user_attributes_for_findings required"
        )
    if "lastAssessmentRunArn" in data:
        out["last_assessment_run_arn"] = data["lastAssessmentRunArn"]
    if "assessmentRunCount" in data:
        out["assessment_run_count"] = data["assessmentRunCount"]
    else:
        raise DeserializationError("AssessmentTemplate.assessment_run_count required")
    if "createdAt" in data:
        import capo_inspector.types.timestamp

        out["created_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AssessmentTemplate.created_at required")
    return out
