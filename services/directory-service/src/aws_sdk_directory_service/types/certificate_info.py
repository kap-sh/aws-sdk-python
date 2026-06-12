"""Generated from Smithy shape ``com.amazonaws.directoryservice#CertificateInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.certificate_cn
    import aws_sdk_directory_service.types.certificate_expiry_date_time
    import aws_sdk_directory_service.types.certificate_id
    import aws_sdk_directory_service.types.certificate_state
    import aws_sdk_directory_service.types.certificate_type


class CertificateInfo(TypedDict):
    certificate_id: NotRequired[
        "aws_sdk_directory_service.types.certificate_id.CertificateId"
    ]
    """<p>The identifier of the certificate.</p>"""
    common_name: NotRequired[
        "aws_sdk_directory_service.types.certificate_cn.CertificateCN"
    ]
    """<p>The common name for the certificate.</p>"""
    state: NotRequired[
        "aws_sdk_directory_service.types.certificate_state.CertificateState"
    ]
    """<p>The state of the certificate.</p>"""
    expiry_date_time: NotRequired[
        "aws_sdk_directory_service.types.certificate_expiry_date_time.CertificateExpiryDateTime"
    ]
    """<p>The date and time when the certificate will expire.</p>"""
    type: NotRequired[
        "aws_sdk_directory_service.types.certificate_type.CertificateType"
    ]
    """<p>The function that the registered certificate performs. Valid values include <code>ClientLDAPS</code> or <code>ClientCertAuth</code>. The default value is <code>ClientLDAPS</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateInfo) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    if "common_name" in value:
        out["CommonName"] = value["common_name"]
    if "state" in value:
        import aws_sdk_directory_service.types.certificate_state

        out["State"] = (
            aws_sdk_directory_service.types.certificate_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "expiry_date_time" in value:
        import aws_sdk_directory_service.types.certificate_expiry_date_time

        out["ExpiryDateTime"] = (
            aws_sdk_directory_service.types.certificate_expiry_date_time.serialize_aws_json_1_1(
                value["expiry_date_time"]
            )
        )
    if "type" in value:
        import aws_sdk_directory_service.types.certificate_type

        out["Type"] = (
            aws_sdk_directory_service.types.certificate_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateInfo:
    out: CertificateInfo = {}  # type: ignore[typeddict-item]
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    if "CommonName" in data:
        out["common_name"] = data["CommonName"]
    if "State" in data:
        import aws_sdk_directory_service.types.certificate_state

        out["state"] = (
            aws_sdk_directory_service.types.certificate_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "ExpiryDateTime" in data:
        import aws_sdk_directory_service.types.certificate_expiry_date_time

        out["expiry_date_time"] = (
            aws_sdk_directory_service.types.certificate_expiry_date_time.deserialize_aws_json_1_1(
                data["ExpiryDateTime"]
            )
        )
    if "Type" in data:
        import aws_sdk_directory_service.types.certificate_type

        out["type"] = (
            aws_sdk_directory_service.types.certificate_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
