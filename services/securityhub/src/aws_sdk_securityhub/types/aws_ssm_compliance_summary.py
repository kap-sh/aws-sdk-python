"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSsmComplianceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsSsmComplianceSummary(TypedDict):
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current patch compliance status. Valid values are as follows:</p> <ul> <li> <p> <code>COMPLIANT</code> </p> </li> <li> <p> <code>NON_COMPLIANT</code> </p> </li> <li> <p> <code>UNSPECIFIED_DATA</code> </p> </li> </ul>"""
    compliant_critical_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>For the patches that are compliant, the number that have a severity of <code>CRITICAL</code>.</p>"""
    compliant_high_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>For the patches that are compliant, the number that have a severity of <code>HIGH</code>.</p>"""
    compliant_medium_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>For the patches that are compliant, the number that have a severity of <code>MEDIUM</code>.</p>"""
    execution_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of execution that was used determine compliance.</p>"""
    non_compliant_critical_count: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>For the patch items that are noncompliant, the number of items that have a severity of <code>CRITICAL</code>.</p>"""
    compliant_informational_count: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>For the patches that are compliant, the number that have a severity of <code>INFORMATIONAL</code>.</p>"""
    non_compliant_informational_count: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>For the patches that are noncompliant, the number that have a severity of <code>INFORMATIONAL</code>.</p>"""
    compliant_unspecified_count: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>For the patches that are compliant, the number that have a severity of <code>UNSPECIFIED</code>.</p>"""
    non_compliant_low_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>For the patches that are noncompliant, the number that have a severity of <code>LOW</code>.</p>"""
    non_compliant_high_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>For the patches that are noncompliant, the number that have a severity of <code>HIGH</code>.</p>"""
    compliant_low_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>For the patches that are compliant, the number that have a severity of <code>LOW</code>.</p>"""
    compliance_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of resource for which the compliance was determined. For <code>AwsSsmPatchCompliance</code>, <code>ComplianceType</code> is <code>Patch</code>. </p>"""
    patch_baseline_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the patch baseline. The patch baseline lists the patches that are approved for installation.</p>"""
    overall_severity: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The highest severity for the patches. Valid values are as follows:</p> <ul> <li> <p> <code>CRITICAL</code> </p> </li> <li> <p> <code>HIGH</code> </p> </li> <li> <p> <code>MEDIUM</code> </p> </li> <li> <p> <code>LOW</code> </p> </li> <li> <p> <code>INFORMATIONAL</code> </p> </li> <li> <p> <code>UNSPECIFIED</code> </p> </li> </ul>"""
    non_compliant_medium_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>For the patches that are noncompliant, the number that have a severity of <code>MEDIUM</code>.</p>"""
    non_compliant_unspecified_count: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>For the patches that are noncompliant, the number that have a severity of <code>UNSPECIFIED</code>.</p>"""
    patch_group: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the patch group for which compliance was determined. A patch group uses tags to group EC2 instances that should have the same patch compliance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSsmComplianceSummary) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "compliant_critical_count" in value:
        out["CompliantCriticalCount"] = value["compliant_critical_count"]
    if "compliant_high_count" in value:
        out["CompliantHighCount"] = value["compliant_high_count"]
    if "compliant_medium_count" in value:
        out["CompliantMediumCount"] = value["compliant_medium_count"]
    if "execution_type" in value:
        out["ExecutionType"] = value["execution_type"]
    if "non_compliant_critical_count" in value:
        out["NonCompliantCriticalCount"] = value["non_compliant_critical_count"]
    if "compliant_informational_count" in value:
        out["CompliantInformationalCount"] = value["compliant_informational_count"]
    if "non_compliant_informational_count" in value:
        out["NonCompliantInformationalCount"] = value[
            "non_compliant_informational_count"
        ]
    if "compliant_unspecified_count" in value:
        out["CompliantUnspecifiedCount"] = value["compliant_unspecified_count"]
    if "non_compliant_low_count" in value:
        out["NonCompliantLowCount"] = value["non_compliant_low_count"]
    if "non_compliant_high_count" in value:
        out["NonCompliantHighCount"] = value["non_compliant_high_count"]
    if "compliant_low_count" in value:
        out["CompliantLowCount"] = value["compliant_low_count"]
    if "compliance_type" in value:
        out["ComplianceType"] = value["compliance_type"]
    if "patch_baseline_id" in value:
        out["PatchBaselineId"] = value["patch_baseline_id"]
    if "overall_severity" in value:
        out["OverallSeverity"] = value["overall_severity"]
    if "non_compliant_medium_count" in value:
        out["NonCompliantMediumCount"] = value["non_compliant_medium_count"]
    if "non_compliant_unspecified_count" in value:
        out["NonCompliantUnspecifiedCount"] = value["non_compliant_unspecified_count"]
    if "patch_group" in value:
        out["PatchGroup"] = value["patch_group"]
    return out


def deserialize_json(data: dict) -> AwsSsmComplianceSummary:
    out: AwsSsmComplianceSummary = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "CompliantCriticalCount" in data:
        out["compliant_critical_count"] = data["CompliantCriticalCount"]
    if "CompliantHighCount" in data:
        out["compliant_high_count"] = data["CompliantHighCount"]
    if "CompliantMediumCount" in data:
        out["compliant_medium_count"] = data["CompliantMediumCount"]
    if "ExecutionType" in data:
        out["execution_type"] = data["ExecutionType"]
    if "NonCompliantCriticalCount" in data:
        out["non_compliant_critical_count"] = data["NonCompliantCriticalCount"]
    if "CompliantInformationalCount" in data:
        out["compliant_informational_count"] = data["CompliantInformationalCount"]
    if "NonCompliantInformationalCount" in data:
        out["non_compliant_informational_count"] = data[
            "NonCompliantInformationalCount"
        ]
    if "CompliantUnspecifiedCount" in data:
        out["compliant_unspecified_count"] = data["CompliantUnspecifiedCount"]
    if "NonCompliantLowCount" in data:
        out["non_compliant_low_count"] = data["NonCompliantLowCount"]
    if "NonCompliantHighCount" in data:
        out["non_compliant_high_count"] = data["NonCompliantHighCount"]
    if "CompliantLowCount" in data:
        out["compliant_low_count"] = data["CompliantLowCount"]
    if "ComplianceType" in data:
        out["compliance_type"] = data["ComplianceType"]
    if "PatchBaselineId" in data:
        out["patch_baseline_id"] = data["PatchBaselineId"]
    if "OverallSeverity" in data:
        out["overall_severity"] = data["OverallSeverity"]
    if "NonCompliantMediumCount" in data:
        out["non_compliant_medium_count"] = data["NonCompliantMediumCount"]
    if "NonCompliantUnspecifiedCount" in data:
        out["non_compliant_unspecified_count"] = data["NonCompliantUnspecifiedCount"]
    if "PatchGroup" in data:
        out["patch_group"] = data["PatchGroup"]
    return out
