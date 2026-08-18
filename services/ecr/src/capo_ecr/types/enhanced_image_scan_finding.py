"""Generated from Smithy shape ``com.amazonaws.ecr#EnhancedImageScanFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.date
    import capo_ecr.types.exploit_available
    import capo_ecr.types.finding_arn
    import capo_ecr.types.finding_description
    import capo_ecr.types.fix_available
    import capo_ecr.types.package_vulnerability_details
    import capo_ecr.types.registry_id
    import capo_ecr.types.remediation
    import capo_ecr.types.resource_list
    import capo_ecr.types.score
    import capo_ecr.types.score_details
    import capo_ecr.types.severity
    import capo_ecr.types.status
    import capo_ecr.types.title
    import capo_ecr.types.type


class EnhancedImageScanFinding(TypedDict, closed=True):
    aws_account_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the image.</p>"""
    description: NotRequired["capo_ecr.types.finding_description.FindingDescription"]
    """<p>The description of the finding.</p>"""
    finding_arn: NotRequired["capo_ecr.types.finding_arn.FindingArn"]
    """<p>The Amazon Resource Number (ARN) of the finding.</p>"""
    first_observed_at: NotRequired["capo_ecr.types.date.Date"]
    """<p>The date and time that the finding was first observed.</p>"""
    last_observed_at: NotRequired["capo_ecr.types.date.Date"]
    """<p>The date and time that the finding was last observed.</p>"""
    package_vulnerability_details: NotRequired[
        "capo_ecr.types.package_vulnerability_details.PackageVulnerabilityDetails"
    ]
    """<p>An object that contains the details of a package vulnerability finding.</p>"""
    remediation: NotRequired["capo_ecr.types.remediation.Remediation"]
    """<p>An object that contains the details about how to remediate a finding.</p>"""
    resources: NotRequired["capo_ecr.types.resource_list.ResourceList"]
    """<p>Contains information on the resources involved in a finding.</p>"""
    score: "capo_ecr.types.score.Score"
    """<p>The Amazon Inspector score given to the finding.</p>"""
    score_details: NotRequired["capo_ecr.types.score_details.ScoreDetails"]
    """<p>An object that contains details of the Amazon Inspector score.</p>"""
    severity: NotRequired["capo_ecr.types.severity.Severity"]
    """<p>The severity of the finding.</p>"""
    status: NotRequired["capo_ecr.types.status.Status"]
    """<p>The status of the finding.</p>"""
    title: NotRequired["capo_ecr.types.title.Title"]
    """<p>The title of the finding.</p>"""
    type: NotRequired["capo_ecr.types.type.Type"]
    """<p>The type of the finding.</p>"""
    updated_at: NotRequired["capo_ecr.types.date.Date"]
    """<p>The date and time the finding was last updated at.</p>"""
    fix_available: NotRequired["capo_ecr.types.fix_available.FixAvailable"]
    """<p>Details on whether a fix is available through a version update. This value can be <code>YES</code>, <code>NO</code>, or <code>PARTIAL</code>. A <code>PARTIAL</code> fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.</p>"""
    exploit_available: NotRequired["capo_ecr.types.exploit_available.ExploitAvailable"]
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
        import capo_ecr.types.date

        out["firstObservedAt"] = capo_ecr.types.date.serialize_aws_json_1_1(
            value["first_observed_at"]
        )
    if "last_observed_at" in value:
        import capo_ecr.types.date

        out["lastObservedAt"] = capo_ecr.types.date.serialize_aws_json_1_1(
            value["last_observed_at"]
        )
    if "package_vulnerability_details" in value:
        import capo_ecr.types.package_vulnerability_details

        out["packageVulnerabilityDetails"] = (
            capo_ecr.types.package_vulnerability_details.serialize_aws_json_1_1(
                value["package_vulnerability_details"]
            )
        )
    if "remediation" in value:
        import capo_ecr.types.remediation

        out["remediation"] = capo_ecr.types.remediation.serialize_aws_json_1_1(
            value["remediation"]
        )
    if "resources" in value:
        import capo_ecr.types.resource_list

        out["resources"] = capo_ecr.types.resource_list.serialize_aws_json_1_1(
            value["resources"]
        )
    out["score"] = (
        "NaN"
        if value.get("score", 0) != value.get("score", 0)
        else "Infinity"
        if value.get("score", 0) == float("inf")
        else "-Infinity"
        if value.get("score", 0) == float("-inf")
        else value.get("score", 0)
    )
    if "score_details" in value:
        import capo_ecr.types.score_details

        out["scoreDetails"] = capo_ecr.types.score_details.serialize_aws_json_1_1(
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
        import capo_ecr.types.date

        out["updatedAt"] = capo_ecr.types.date.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "fix_available" in value:
        out["fixAvailable"] = value["fix_available"]
    if "exploit_available" in value:
        out["exploitAvailable"] = value["exploit_available"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnhancedImageScanFinding:
    out: EnhancedImageScanFinding = {}  # type: ignore[typeddict-item]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("findingArn") is not None:
        out["finding_arn"] = data["findingArn"]
    if data.get("firstObservedAt") is not None:
        import capo_ecr.types.date

        out["first_observed_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(
            data["firstObservedAt"]
        )
    if data.get("lastObservedAt") is not None:
        import capo_ecr.types.date

        out["last_observed_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(
            data["lastObservedAt"]
        )
    if data.get("packageVulnerabilityDetails") is not None:
        import capo_ecr.types.package_vulnerability_details

        out["package_vulnerability_details"] = (
            capo_ecr.types.package_vulnerability_details.deserialize_aws_json_1_1(
                data["packageVulnerabilityDetails"]
            )
        )
    if data.get("remediation") is not None:
        import capo_ecr.types.remediation

        out["remediation"] = capo_ecr.types.remediation.deserialize_aws_json_1_1(
            data["remediation"]
        )
    if data.get("resources") is not None:
        import capo_ecr.types.resource_list

        out["resources"] = capo_ecr.types.resource_list.deserialize_aws_json_1_1(
            data["resources"]
        )
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    else:
        out["score"] = 0
    if data.get("scoreDetails") is not None:
        import capo_ecr.types.score_details

        out["score_details"] = capo_ecr.types.score_details.deserialize_aws_json_1_1(
            data["scoreDetails"]
        )
    if data.get("severity") is not None:
        out["severity"] = data["severity"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("updatedAt") is not None:
        import capo_ecr.types.date

        out["updated_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    if data.get("fixAvailable") is not None:
        out["fix_available"] = data["fixAvailable"]
    if data.get("exploitAvailable") is not None:
        out["exploit_available"] = data["exploitAvailable"]
    return out
