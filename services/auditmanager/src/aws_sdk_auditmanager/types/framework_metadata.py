"""Generated from Smithy shape ``com.amazonaws.auditmanager#FrameworkMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_framework_description
    import aws_sdk_auditmanager.types.assessment_name
    import aws_sdk_auditmanager.types.compliance_type
    import aws_sdk_auditmanager.types.filename


class FrameworkMetadata(TypedDict):
    name: NotRequired["aws_sdk_auditmanager.types.assessment_name.AssessmentName"]
    """<p> The name of the framework. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.assessment_framework_description.AssessmentFrameworkDescription"
    ]
    """<p> The description of the framework. </p>"""
    logo: NotRequired["aws_sdk_auditmanager.types.filename.Filename"]
    """<p> The logo that's associated with the framework. </p>"""
    compliance_type: NotRequired[
        "aws_sdk_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance standard that's associated with the framework. For example, this could be PCI DSS or HIPAA. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "logo" in value:
        out["logo"] = value["logo"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    return out


def deserialize_json(data: dict) -> FrameworkMetadata:
    out: FrameworkMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "logo" in data:
        out["logo"] = data["logo"]
    if "complianceType" in data:
        out["compliance_type"] = data["complianceType"]
    return out
