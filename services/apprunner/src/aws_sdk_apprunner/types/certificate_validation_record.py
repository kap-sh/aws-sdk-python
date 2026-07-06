"""Generated from Smithy shape ``com.amazonaws.apprunner#CertificateValidationRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.certificate_validation_record_status
    import aws_sdk_apprunner.types.string


class CertificateValidationRecord(TypedDict, closed=True):
    name: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The certificate CNAME record name.</p>"""
    type: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The record type, always <code>CNAME</code>.</p>"""
    value: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The certificate CNAME record value.</p>"""
    status: NotRequired[
        "aws_sdk_apprunner.types.certificate_validation_record_status.CertificateValidationRecordStatus"
    ]
    """<p>The current state of the certificate CNAME record validation. It should change to <code>SUCCESS</code> after App Runner completes validation with your DNS.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CertificateValidationRecord) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    if "status" in value:
        import aws_sdk_apprunner.types.certificate_validation_record_status

        out["Status"] = (
            aws_sdk_apprunner.types.certificate_validation_record_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CertificateValidationRecord:
    out: CertificateValidationRecord = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Status" in data:
        import aws_sdk_apprunner.types.certificate_validation_record_status

        out["status"] = (
            aws_sdk_apprunner.types.certificate_validation_record_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
