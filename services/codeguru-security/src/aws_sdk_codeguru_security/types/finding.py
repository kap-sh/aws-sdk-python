"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#Finding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_codeguru_security.types.detector_tags
    import aws_sdk_codeguru_security.types.remediation
    import aws_sdk_codeguru_security.types.resource
    import aws_sdk_codeguru_security.types.severity
    import aws_sdk_codeguru_security.types.status
    import aws_sdk_codeguru_security.types.vulnerability


class Finding(TypedDict):
    created_at: NotRequired["datetime.datetime"]
    """<p>The time when the finding was created.</p>"""
    description: NotRequired["str"]
    """<p>A description of the finding.</p>"""
    generator_id: NotRequired["str"]
    """<p>The identifier for the component that generated a finding such as AmazonCodeGuruSecurity.</p>"""
    id: NotRequired["str"]
    """<p>The identifier for a finding.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time when the finding was last updated. Findings are updated when you remediate them or when the finding code location changes. </p>"""
    type: NotRequired["str"]
    """<p>The type of finding. </p>"""
    status: NotRequired["aws_sdk_codeguru_security.types.status.Status"]
    """<p>The status of the finding. A finding status can be open or closed. </p>"""
    resource: NotRequired["aws_sdk_codeguru_security.types.resource.Resource"]
    """<p>The resource where Amazon CodeGuru Security detected a finding.</p>"""
    vulnerability: NotRequired[
        "aws_sdk_codeguru_security.types.vulnerability.Vulnerability"
    ]
    """<p>An object that describes the detected security vulnerability.</p>"""
    severity: NotRequired["aws_sdk_codeguru_security.types.severity.Severity"]
    """<p>The severity of the finding. Severity can be critical, high, medium, low, or informational. For information on severity levels, see <a href=\"https://docs.aws.amazon.com/codeguru/latest/security-ug/findings-overview.html#severity-distribution\">Finding severity</a> in the <i>Amazon CodeGuru Security User Guide</i>.</p>"""
    remediation: NotRequired["aws_sdk_codeguru_security.types.remediation.Remediation"]
    """<p>An object that contains the details about how to remediate a finding.</p>"""
    title: NotRequired["str"]
    """<p>The title of the finding.</p>"""
    detector_tags: NotRequired[
        "aws_sdk_codeguru_security.types.detector_tags.DetectorTags"
    ]
    """<p>One or more tags or categorizations that are associated with a detector. These tags are defined by type, programming language, or other classification such as maintainability or consistency.</p>"""
    detector_id: NotRequired["str"]
    """<p>The identifier for the detector that detected the finding in your code. A detector is a defined rule based on industry standards and AWS best practices. </p>"""
    detector_name: NotRequired["str"]
    """<p>The name of the detector that identified the security vulnerability in your code. </p>"""
    rule_id: NotRequired["str"]
    """<p>The identifier for the rule that generated the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    if "created_at" in value:
        import aws_sdk_codeguru_security.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_codeguru_security.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "generator_id" in value:
        out["generatorId"] = value["generator_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "updated_at" in value:
        import aws_sdk_codeguru_security.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_codeguru_security.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    if "type" in value:
        out["type"] = value["type"]
    if "status" in value:
        import aws_sdk_codeguru_security.types.status

        out["status"] = aws_sdk_codeguru_security.types.status.serialize_json(
            value["status"]
        )
    if "resource" in value:
        import aws_sdk_codeguru_security.types.resource

        out["resource"] = aws_sdk_codeguru_security.types.resource.serialize_json(
            value["resource"]
        )
    if "vulnerability" in value:
        import aws_sdk_codeguru_security.types.vulnerability

        out["vulnerability"] = (
            aws_sdk_codeguru_security.types.vulnerability.serialize_json(
                value["vulnerability"]
            )
        )
    if "severity" in value:
        import aws_sdk_codeguru_security.types.severity

        out["severity"] = aws_sdk_codeguru_security.types.severity.serialize_json(
            value["severity"]
        )
    if "remediation" in value:
        import aws_sdk_codeguru_security.types.remediation

        out["remediation"] = aws_sdk_codeguru_security.types.remediation.serialize_json(
            value["remediation"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "detector_tags" in value:
        import aws_sdk_codeguru_security.types.detector_tags

        out["detectorTags"] = (
            aws_sdk_codeguru_security.types.detector_tags.serialize_json(
                value["detector_tags"]
            )
        )
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "detector_name" in value:
        out["detectorName"] = value["detector_name"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if "createdAt" in data:
        import aws_sdk_codeguru_security.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "generatorId" in data:
        out["generator_id"] = data["generatorId"]
    if "id" in data:
        out["id"] = data["id"]
    if "updatedAt" in data:
        import aws_sdk_codeguru_security.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "type" in data:
        out["type"] = data["type"]
    if "status" in data:
        import aws_sdk_codeguru_security.types.status

        out["status"] = aws_sdk_codeguru_security.types.status.deserialize_json(
            data["status"]
        )
    if "resource" in data:
        import aws_sdk_codeguru_security.types.resource

        out["resource"] = aws_sdk_codeguru_security.types.resource.deserialize_json(
            data["resource"]
        )
    if "vulnerability" in data:
        import aws_sdk_codeguru_security.types.vulnerability

        out["vulnerability"] = (
            aws_sdk_codeguru_security.types.vulnerability.deserialize_json(
                data["vulnerability"]
            )
        )
    if "severity" in data:
        import aws_sdk_codeguru_security.types.severity

        out["severity"] = aws_sdk_codeguru_security.types.severity.deserialize_json(
            data["severity"]
        )
    if "remediation" in data:
        import aws_sdk_codeguru_security.types.remediation

        out["remediation"] = (
            aws_sdk_codeguru_security.types.remediation.deserialize_json(
                data["remediation"]
            )
        )
    if "title" in data:
        out["title"] = data["title"]
    if "detectorTags" in data:
        import aws_sdk_codeguru_security.types.detector_tags

        out["detector_tags"] = (
            aws_sdk_codeguru_security.types.detector_tags.deserialize_json(
                data["detectorTags"]
            )
        )
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "detectorName" in data:
        out["detector_name"] = data["detectorName"]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    return out
