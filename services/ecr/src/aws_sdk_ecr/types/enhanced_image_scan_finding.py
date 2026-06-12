"""Generated from Smithy shape ``com.amazonaws.ecr#EnhancedImageScanFinding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.date
    import aws_sdk_ecr.types.exploit_available
    import aws_sdk_ecr.types.finding_arn
    import aws_sdk_ecr.types.finding_description
    import aws_sdk_ecr.types.fix_available
    import aws_sdk_ecr.types.package_vulnerability_details
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.remediation
    import aws_sdk_ecr.types.resource_list
    import aws_sdk_ecr.types.score
    import aws_sdk_ecr.types.score_details
    import aws_sdk_ecr.types.severity
    import aws_sdk_ecr.types.status
    import aws_sdk_ecr.types.title
    import aws_sdk_ecr.types.type


class EnhancedImageScanFinding(TypedDict):
    aws_account_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the image.</p>"""
    description: NotRequired["aws_sdk_ecr.types.finding_description.FindingDescription"]
    """<p>The description of the finding.</p>"""
    finding_arn: NotRequired["aws_sdk_ecr.types.finding_arn.FindingArn"]
    """<p>The Amazon Resource Number (ARN) of the finding.</p>"""
    first_observed_at: NotRequired["aws_sdk_ecr.types.date.Date"]
    """<p>The date and time that the finding was first observed.</p>"""
    last_observed_at: NotRequired["aws_sdk_ecr.types.date.Date"]
    """<p>The date and time that the finding was last observed.</p>"""
    package_vulnerability_details: NotRequired[
        "aws_sdk_ecr.types.package_vulnerability_details.PackageVulnerabilityDetails"
    ]
    """<p>An object that contains the details of a package vulnerability finding.</p>"""
    remediation: NotRequired["aws_sdk_ecr.types.remediation.Remediation"]
    """<p>An object that contains the details about how to remediate a finding.</p>"""
    resources: NotRequired["aws_sdk_ecr.types.resource_list.ResourceList"]
    """<p>Contains information on the resources involved in a finding.</p>"""
    score: "aws_sdk_ecr.types.score.Score"
    """<p>The Amazon Inspector score given to the finding.</p>"""
    score_details: NotRequired["aws_sdk_ecr.types.score_details.ScoreDetails"]
    """<p>An object that contains details of the Amazon Inspector score.</p>"""
    severity: NotRequired["aws_sdk_ecr.types.severity.Severity"]
    """<p>The severity of the finding.</p>"""
    status: NotRequired["aws_sdk_ecr.types.status.Status"]
    """<p>The status of the finding.</p>"""
    title: NotRequired["aws_sdk_ecr.types.title.Title"]
    """<p>The title of the finding.</p>"""
    type: NotRequired["aws_sdk_ecr.types.type.Type"]
    """<p>The type of the finding.</p>"""
    updated_at: NotRequired["aws_sdk_ecr.types.date.Date"]
    """<p>The date and time the finding was last updated at.</p>"""
    fix_available: NotRequired["aws_sdk_ecr.types.fix_available.FixAvailable"]
    """<p>Details on whether a fix is available through a version update. This value can be <code>YES</code>, <code>NO</code>, or <code>PARTIAL</code>. A <code>PARTIAL</code> fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.</p>"""
    exploit_available: NotRequired[
        "aws_sdk_ecr.types.exploit_available.ExploitAvailable"
    ]
    """<p>If a finding discovered in your environment has an exploit available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnhancedImageScanFinding) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "finding_arn" in value:
        out["findingArn"] = value["finding_arn"]
    if "first_observed_at" in value:
        import aws_sdk_ecr.types.date

        out["firstObservedAt"] = aws_sdk_ecr.types.date.serialize_aws_json_1_1(
            value["first_observed_at"]
        )
    if "last_observed_at" in value:
        import aws_sdk_ecr.types.date

        out["lastObservedAt"] = aws_sdk_ecr.types.date.serialize_aws_json_1_1(
            value["last_observed_at"]
        )
    if "package_vulnerability_details" in value:
        import aws_sdk_ecr.types.package_vulnerability_details

        out["packageVulnerabilityDetails"] = (
            aws_sdk_ecr.types.package_vulnerability_details.serialize_aws_json_1_1(
                value["package_vulnerability_details"]
            )
        )
    if "remediation" in value:
        import aws_sdk_ecr.types.remediation

        out["remediation"] = aws_sdk_ecr.types.remediation.serialize_aws_json_1_1(
            value["remediation"]
        )
    if "resources" in value:
        import aws_sdk_ecr.types.resource_list

        out["resources"] = aws_sdk_ecr.types.resource_list.serialize_aws_json_1_1(
            value["resources"]
        )
    out["score"] = value.get("score", 0)
    if "score_details" in value:
        import aws_sdk_ecr.types.score_details

        out["scoreDetails"] = aws_sdk_ecr.types.score_details.serialize_aws_json_1_1(
            value["score_details"]
        )
    if "severity" in value:
        out["severity"] = value["severity"]
    if "status" in value:
        out["status"] = value["status"]
    if "title" in value:
        out["title"] = value["title"]
    if "type" in value:
        out["type"] = value["type"]
    if "updated_at" in value:
        import aws_sdk_ecr.types.date

        out["updatedAt"] = aws_sdk_ecr.types.date.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "fix_available" in value:
        out["fixAvailable"] = value["fix_available"]
    if "exploit_available" in value:
        out["exploitAvailable"] = value["exploit_available"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnhancedImageScanFinding:
    out: EnhancedImageScanFinding = {}  # type: ignore[typeddict-item]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "description" in data:
        out["description"] = data["description"]
    if "findingArn" in data:
        out["finding_arn"] = data["findingArn"]
    if "firstObservedAt" in data:
        import aws_sdk_ecr.types.date

        out["first_observed_at"] = aws_sdk_ecr.types.date.deserialize_aws_json_1_1(
            data["firstObservedAt"]
        )
    if "lastObservedAt" in data:
        import aws_sdk_ecr.types.date

        out["last_observed_at"] = aws_sdk_ecr.types.date.deserialize_aws_json_1_1(
            data["lastObservedAt"]
        )
    if "packageVulnerabilityDetails" in data:
        import aws_sdk_ecr.types.package_vulnerability_details

        out["package_vulnerability_details"] = (
            aws_sdk_ecr.types.package_vulnerability_details.deserialize_aws_json_1_1(
                data["packageVulnerabilityDetails"]
            )
        )
    if "remediation" in data:
        import aws_sdk_ecr.types.remediation

        out["remediation"] = aws_sdk_ecr.types.remediation.deserialize_aws_json_1_1(
            data["remediation"]
        )
    if "resources" in data:
        import aws_sdk_ecr.types.resource_list

        out["resources"] = aws_sdk_ecr.types.resource_list.deserialize_aws_json_1_1(
            data["resources"]
        )
    if "score" in data:
        out["score"] = data["score"]
    else:
        out["score"] = 0
    if "scoreDetails" in data:
        import aws_sdk_ecr.types.score_details

        out["score_details"] = aws_sdk_ecr.types.score_details.deserialize_aws_json_1_1(
            data["scoreDetails"]
        )
    if "severity" in data:
        out["severity"] = data["severity"]
    if "status" in data:
        out["status"] = data["status"]
    if "title" in data:
        out["title"] = data["title"]
    if "type" in data:
        out["type"] = data["type"]
    if "updatedAt" in data:
        import aws_sdk_ecr.types.date

        out["updated_at"] = aws_sdk_ecr.types.date.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    if "fixAvailable" in data:
        out["fix_available"] = data["fixAvailable"]
    if "exploitAvailable" in data:
        out["exploit_available"] = data["exploitAvailable"]
    return out
