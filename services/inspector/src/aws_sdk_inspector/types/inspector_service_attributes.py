"""Generated from Smithy shape ``com.amazonaws.inspector#InspectorServiceAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.numeric_version


class InspectorServiceAttributes(TypedDict):
    schema_version: "aws_sdk_inspector.types.numeric_version.NumericVersion"
    """<p>The schema version of this data type.</p>"""
    assessment_run_arn: NotRequired["aws_sdk_inspector.types.arn.Arn"]
    """<p>The ARN of the assessment run during which the finding is generated.</p>"""
    rules_package_arn: NotRequired["aws_sdk_inspector.types.arn.Arn"]
    """<p>The ARN of the rules package that is used to generate the finding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InspectorServiceAttributes) -> dict:
    out: dict = {}
    out["schemaVersion"] = value.get("schema_version", 0)
    if "assessment_run_arn" in value:
        out["assessmentRunArn"] = value["assessment_run_arn"]
    if "rules_package_arn" in value:
        out["rulesPackageArn"] = value["rules_package_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InspectorServiceAttributes:
    out: InspectorServiceAttributes = {}  # type: ignore[typeddict-item]
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        out["schema_version"] = 0
    if "assessmentRunArn" in data:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    if "rulesPackageArn" in data:
        out["rules_package_arn"] = data["rulesPackageArn"]
    return out
