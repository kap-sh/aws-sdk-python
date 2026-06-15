"""Generated from Smithy shape ``com.amazonaws.ssm#PatchComplianceData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.patch_classification
    import aws_sdk_ssm.types.patch_compliance_data_state
    import aws_sdk_ssm.types.patch_cve_ids
    import aws_sdk_ssm.types.patch_kb_number
    import aws_sdk_ssm.types.patch_severity
    import aws_sdk_ssm.types.patch_title


class PatchComplianceData(TypedDict):
    title: "aws_sdk_ssm.types.patch_title.PatchTitle"
    """<p>The title of the patch.</p>"""
    kb_id: "aws_sdk_ssm.types.patch_kb_number.PatchKbNumber"
    """<p>The operating system-specific ID of the patch.</p>"""
    classification: "aws_sdk_ssm.types.patch_classification.PatchClassification"
    """<p>The classification of the patch, such as <code>SecurityUpdates</code>, <code>Updates</code>, and <code>CriticalUpdates</code>.</p>"""
    severity: "aws_sdk_ssm.types.patch_severity.PatchSeverity"
    """<p>The severity of the patch such as <code>Critical</code>, <code>Important</code>, and <code>Moderate</code>.</p>"""
    state: "aws_sdk_ssm.types.patch_compliance_data_state.PatchComplianceDataState"
    r"""<p>The state of the patch on the managed node, such as INSTALLED or FAILED.</p> <p>For descriptions of each patch state, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-about.html#compliance-monitor-patch\">About patch compliance</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    installed_time: "aws_sdk_ssm.types.date_time.DateTime"
    """<p>The date/time the patch was installed on the managed node. Not all operating systems provide this level of information.</p>"""
    cve_ids: NotRequired["aws_sdk_ssm.types.patch_cve_ids.PatchCVEIds"]
    """<p>The IDs of one or more Common Vulnerabilities and Exposure (CVE) issues that are resolved by the patch.</p> <note> <p>Currently, CVE ID values are reported only for patches with a status of <code>Missing</code> or <code>Failed</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchComplianceData) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    out["KBId"] = value["kb_id"]
    out["Classification"] = value["classification"]
    out["Severity"] = value["severity"]
    import aws_sdk_ssm.types.patch_compliance_data_state

    out["State"] = aws_sdk_ssm.types.patch_compliance_data_state.serialize_aws_json_1_1(
        value["state"]
    )
    import aws_sdk_ssm.types.date_time

    out["InstalledTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
        value["installed_time"]
    )
    if "cve_ids" in value:
        out["CVEIds"] = value["cve_ids"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchComplianceData:
    out: PatchComplianceData = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("PatchComplianceData.title required")
    if "KBId" in data:
        out["kb_id"] = data["KBId"]
    else:
        raise DeserializationError("PatchComplianceData.kb_id required")
    if "Classification" in data:
        out["classification"] = data["Classification"]
    else:
        raise DeserializationError("PatchComplianceData.classification required")
    if "Severity" in data:
        out["severity"] = data["Severity"]
    else:
        raise DeserializationError("PatchComplianceData.severity required")
    if "State" in data:
        import aws_sdk_ssm.types.patch_compliance_data_state

        out["state"] = (
            aws_sdk_ssm.types.patch_compliance_data_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    else:
        raise DeserializationError("PatchComplianceData.state required")
    if "InstalledTime" in data:
        import aws_sdk_ssm.types.date_time

        out["installed_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["InstalledTime"]
        )
    else:
        raise DeserializationError("PatchComplianceData.installed_time required")
    if "CVEIds" in data:
        out["cve_ids"] = data["CVEIds"]
    return out
