"""Generated from Smithy shape ``com.amazonaws.inspector2#Finding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.code_vulnerability_details
    import aws_sdk_inspector2.types.date_time_timestamp
    import aws_sdk_inspector2.types.epss_details
    import aws_sdk_inspector2.types.exploit_available
    import aws_sdk_inspector2.types.exploitability_details
    import aws_sdk_inspector2.types.finding_arn
    import aws_sdk_inspector2.types.finding_description
    import aws_sdk_inspector2.types.finding_status
    import aws_sdk_inspector2.types.finding_title
    import aws_sdk_inspector2.types.finding_type
    import aws_sdk_inspector2.types.fix_available
    import aws_sdk_inspector2.types.inspector_score_details
    import aws_sdk_inspector2.types.network_reachability_details
    import aws_sdk_inspector2.types.package_vulnerability_details
    import aws_sdk_inspector2.types.remediation
    import aws_sdk_inspector2.types.resource_list
    import aws_sdk_inspector2.types.severity


class Finding(TypedDict):
    finding_arn: "aws_sdk_inspector2.types.finding_arn.FindingArn"
    """<p>The Amazon Resource Number (ARN) of the finding.</p>"""
    aws_account_id: "aws_sdk_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID associated with the finding.</p>"""
    type: "aws_sdk_inspector2.types.finding_type.FindingType"
    r"""<p>The type of the finding. The <code>type</code> value determines the valid values for <code>resource</code> in your request. For more information, see <a href=\"https://docs.aws.amazon.com/inspector/latest/user/findings-types.html\">Finding types</a> in the Amazon Inspector user guide.</p>"""
    description: "aws_sdk_inspector2.types.finding_description.FindingDescription"
    """<p>The description of the finding.</p>"""
    title: NotRequired["aws_sdk_inspector2.types.finding_title.FindingTitle"]
    """<p>The title of the finding.</p>"""
    remediation: "aws_sdk_inspector2.types.remediation.Remediation"
    """<p>An object that contains the details about how to remediate a finding.</p>"""
    severity: "aws_sdk_inspector2.types.severity.Severity"
    r"""<p>The severity of the finding. <code>UNTRIAGED</code> applies to <code>PACKAGE_VULNERABILITY</code> type findings that the vendor has not assigned a severity yet. For more information, see <a href=\"https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html\">Severity levels for findings</a> in the Amazon Inspector user guide.</p>"""
    first_observed_at: "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    """<p>The date and time that the finding was first observed.</p>"""
    last_observed_at: "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    """<p> The date and time the finding was last observed. This timestamp for this field remains unchanged until a finding is updated. </p>"""
    updated_at: NotRequired[
        "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the finding was last updated at.</p>"""
    status: "aws_sdk_inspector2.types.finding_status.FindingStatus"
    """<p>The status of the finding.</p>"""
    resources: "aws_sdk_inspector2.types.resource_list.ResourceList"
    r"""<p>Contains information on the resources involved in a finding. The <code>resource</code> value determines the valid values for <code>type</code> in your request. For more information, see <a href=\"https://docs.aws.amazon.com/inspector/latest/user/findings-types.html\">Finding types</a> in the Amazon Inspector user guide.</p>"""
    inspector_score: NotRequired["float"]
    """<p>The Amazon Inspector score given to the finding.</p>"""
    inspector_score_details: NotRequired[
        "aws_sdk_inspector2.types.inspector_score_details.InspectorScoreDetails"
    ]
    """<p>An object that contains details of the Amazon Inspector score.</p>"""
    network_reachability_details: NotRequired[
        "aws_sdk_inspector2.types.network_reachability_details.NetworkReachabilityDetails"
    ]
    """<p>An object that contains the details of a network reachability finding.</p>"""
    package_vulnerability_details: NotRequired[
        "aws_sdk_inspector2.types.package_vulnerability_details.PackageVulnerabilityDetails"
    ]
    """<p>An object that contains the details of a package vulnerability finding.</p>"""
    fix_available: NotRequired["aws_sdk_inspector2.types.fix_available.FixAvailable"]
    """<p>Details on whether a fix is available through a version update. This value can be <code>YES</code>, <code>NO</code>, or <code>PARTIAL</code>. A <code>PARTIAL</code> fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.</p>"""
    exploit_available: NotRequired[
        "aws_sdk_inspector2.types.exploit_available.ExploitAvailable"
    ]
    """<p>If a finding discovered in your environment has an exploit available.</p>"""
    exploitability_details: NotRequired[
        "aws_sdk_inspector2.types.exploitability_details.ExploitabilityDetails"
    ]
    """<p>The details of an exploit available for a finding discovered in your environment.</p>"""
    code_vulnerability_details: NotRequired[
        "aws_sdk_inspector2.types.code_vulnerability_details.CodeVulnerabilityDetails"
    ]
    """<p>Details about the code vulnerability identified in a Lambda function used to filter findings.</p>"""
    epss: NotRequired["aws_sdk_inspector2.types.epss_details.EpssDetails"]
    """<p>The finding's EPSS score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    out["findingArn"] = value["finding_arn"]
    out["awsAccountId"] = value["aws_account_id"]
    out["type"] = value["type"]
    out["description"] = value["description"]
    if "title" in value:
        out["title"] = value["title"]
    import aws_sdk_inspector2.types.remediation

    out["remediation"] = aws_sdk_inspector2.types.remediation.serialize_json(
        value["remediation"]
    )
    out["severity"] = value["severity"]
    import aws_sdk_inspector2.types.date_time_timestamp

    out["firstObservedAt"] = (
        aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
            value["first_observed_at"]
        )
    )
    import aws_sdk_inspector2.types.date_time_timestamp

    out["lastObservedAt"] = aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
        value["last_observed_at"]
    )
    if "updated_at" in value:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["updatedAt"] = aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
            value["updated_at"]
        )
    out["status"] = value["status"]
    import aws_sdk_inspector2.types.resource_list

    out["resources"] = aws_sdk_inspector2.types.resource_list.serialize_json(
        value["resources"]
    )
    if "inspector_score" in value:
        out["inspectorScore"] = value["inspector_score"]
    if "inspector_score_details" in value:
        import aws_sdk_inspector2.types.inspector_score_details

        out["inspectorScoreDetails"] = (
            aws_sdk_inspector2.types.inspector_score_details.serialize_json(
                value["inspector_score_details"]
            )
        )
    if "network_reachability_details" in value:
        import aws_sdk_inspector2.types.network_reachability_details

        out["networkReachabilityDetails"] = (
            aws_sdk_inspector2.types.network_reachability_details.serialize_json(
                value["network_reachability_details"]
            )
        )
    if "package_vulnerability_details" in value:
        import aws_sdk_inspector2.types.package_vulnerability_details

        out["packageVulnerabilityDetails"] = (
            aws_sdk_inspector2.types.package_vulnerability_details.serialize_json(
                value["package_vulnerability_details"]
            )
        )
    if "fix_available" in value:
        out["fixAvailable"] = value["fix_available"]
    if "exploit_available" in value:
        out["exploitAvailable"] = value["exploit_available"]
    if "exploitability_details" in value:
        import aws_sdk_inspector2.types.exploitability_details

        out["exploitabilityDetails"] = (
            aws_sdk_inspector2.types.exploitability_details.serialize_json(
                value["exploitability_details"]
            )
        )
    if "code_vulnerability_details" in value:
        import aws_sdk_inspector2.types.code_vulnerability_details

        out["codeVulnerabilityDetails"] = (
            aws_sdk_inspector2.types.code_vulnerability_details.serialize_json(
                value["code_vulnerability_details"]
            )
        )
    if "epss" in value:
        import aws_sdk_inspector2.types.epss_details

        out["epss"] = aws_sdk_inspector2.types.epss_details.serialize_json(
            value["epss"]
        )
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if "findingArn" in data:
        out["finding_arn"] = data["findingArn"]
    else:
        raise DeserializationError("Finding.finding_arn required")
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    else:
        raise DeserializationError("Finding.aws_account_id required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Finding.type required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("Finding.description required")
    if "title" in data:
        out["title"] = data["title"]
    if "remediation" in data:
        import aws_sdk_inspector2.types.remediation

        out["remediation"] = aws_sdk_inspector2.types.remediation.deserialize_json(
            data["remediation"]
        )
    else:
        raise DeserializationError("Finding.remediation required")
    if "severity" in data:
        out["severity"] = data["severity"]
    else:
        raise DeserializationError("Finding.severity required")
    if "firstObservedAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["first_observed_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["firstObservedAt"]
            )
        )
    else:
        raise DeserializationError("Finding.first_observed_at required")
    if "lastObservedAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["last_observed_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastObservedAt"]
            )
        )
    else:
        raise DeserializationError("Finding.last_observed_at required")
    if "updatedAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["updated_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("Finding.status required")
    if "resources" in data:
        import aws_sdk_inspector2.types.resource_list

        out["resources"] = aws_sdk_inspector2.types.resource_list.deserialize_json(
            data["resources"]
        )
    else:
        raise DeserializationError("Finding.resources required")
    if "inspectorScore" in data:
        out["inspector_score"] = data["inspectorScore"]
    if "inspectorScoreDetails" in data:
        import aws_sdk_inspector2.types.inspector_score_details

        out["inspector_score_details"] = (
            aws_sdk_inspector2.types.inspector_score_details.deserialize_json(
                data["inspectorScoreDetails"]
            )
        )
    if "networkReachabilityDetails" in data:
        import aws_sdk_inspector2.types.network_reachability_details

        out["network_reachability_details"] = (
            aws_sdk_inspector2.types.network_reachability_details.deserialize_json(
                data["networkReachabilityDetails"]
            )
        )
    if "packageVulnerabilityDetails" in data:
        import aws_sdk_inspector2.types.package_vulnerability_details

        out["package_vulnerability_details"] = (
            aws_sdk_inspector2.types.package_vulnerability_details.deserialize_json(
                data["packageVulnerabilityDetails"]
            )
        )
    if "fixAvailable" in data:
        out["fix_available"] = data["fixAvailable"]
    if "exploitAvailable" in data:
        out["exploit_available"] = data["exploitAvailable"]
    if "exploitabilityDetails" in data:
        import aws_sdk_inspector2.types.exploitability_details

        out["exploitability_details"] = (
            aws_sdk_inspector2.types.exploitability_details.deserialize_json(
                data["exploitabilityDetails"]
            )
        )
    if "codeVulnerabilityDetails" in data:
        import aws_sdk_inspector2.types.code_vulnerability_details

        out["code_vulnerability_details"] = (
            aws_sdk_inspector2.types.code_vulnerability_details.deserialize_json(
                data["codeVulnerabilityDetails"]
            )
        )
    if "epss" in data:
        import aws_sdk_inspector2.types.epss_details

        out["epss"] = aws_sdk_inspector2.types.epss_details.deserialize_json(
            data["epss"]
        )
    return out
