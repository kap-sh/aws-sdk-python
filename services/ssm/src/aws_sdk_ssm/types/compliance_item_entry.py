"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceItemEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_item_details
    import aws_sdk_ssm.types.compliance_item_id
    import aws_sdk_ssm.types.compliance_item_title
    import aws_sdk_ssm.types.compliance_severity
    import aws_sdk_ssm.types.compliance_status


class ComplianceItemEntry(TypedDict):
    id: NotRequired["aws_sdk_ssm.types.compliance_item_id.ComplianceItemId"]
    """<p>The compliance item ID. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article.</p>"""
    title: NotRequired["aws_sdk_ssm.types.compliance_item_title.ComplianceItemTitle"]
    """<p>The title of the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services. </p>"""
    severity: "aws_sdk_ssm.types.compliance_severity.ComplianceSeverity"
    """<p>The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.</p>"""
    status: "aws_sdk_ssm.types.compliance_status.ComplianceStatus"
    """<p>The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.</p>"""
    details: NotRequired[
        "aws_sdk_ssm.types.compliance_item_details.ComplianceItemDetails"
    ]
    """<p>A \"Key\": \"Value\" tag combination for the compliance item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceItemEntry) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "title" in value:
        out["Title"] = value["title"]
    import aws_sdk_ssm.types.compliance_severity

    out["Severity"] = aws_sdk_ssm.types.compliance_severity.serialize_aws_json_1_1(
        value["severity"]
    )
    import aws_sdk_ssm.types.compliance_status

    out["Status"] = aws_sdk_ssm.types.compliance_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "details" in value:
        import aws_sdk_ssm.types.compliance_item_details

        out["Details"] = (
            aws_sdk_ssm.types.compliance_item_details.serialize_aws_json_1_1(
                value["details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceItemEntry:
    out: ComplianceItemEntry = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Severity" in data:
        import aws_sdk_ssm.types.compliance_severity

        out["severity"] = (
            aws_sdk_ssm.types.compliance_severity.deserialize_aws_json_1_1(
                data["Severity"]
            )
        )
    else:
        raise DeserializationError("ComplianceItemEntry.severity required")
    if "Status" in data:
        import aws_sdk_ssm.types.compliance_status

        out["status"] = aws_sdk_ssm.types.compliance_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        raise DeserializationError("ComplianceItemEntry.status required")
    if "Details" in data:
        import aws_sdk_ssm.types.compliance_item_details

        out["details"] = (
            aws_sdk_ssm.types.compliance_item_details.deserialize_aws_json_1_1(
                data["Details"]
            )
        )
    return out
