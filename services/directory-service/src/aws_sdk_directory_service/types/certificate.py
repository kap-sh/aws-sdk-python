"""Generated from Smithy shape ``com.amazonaws.directoryservice#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.certificate_cn
    import aws_sdk_directory_service.types.certificate_expiry_date_time
    import aws_sdk_directory_service.types.certificate_id
    import aws_sdk_directory_service.types.certificate_registered_date_time
    import aws_sdk_directory_service.types.certificate_state
    import aws_sdk_directory_service.types.certificate_state_reason
    import aws_sdk_directory_service.types.certificate_type
    import aws_sdk_directory_service.types.client_cert_auth_settings


class Certificate(TypedDict, closed=True):
    certificate_id: NotRequired[
        "aws_sdk_directory_service.types.certificate_id.CertificateId"
    ]
    """<p>The identifier of the certificate.</p>"""
    state: NotRequired[
        "aws_sdk_directory_service.types.certificate_state.CertificateState"
    ]
    """<p>The state of the certificate.</p>"""
    state_reason: NotRequired[
        "aws_sdk_directory_service.types.certificate_state_reason.CertificateStateReason"
    ]
    """<p>Describes a state change for the certificate.</p>"""
    common_name: NotRequired[
        "aws_sdk_directory_service.types.certificate_cn.CertificateCN"
    ]
    """<p>The common name for the certificate.</p>"""
    registered_date_time: NotRequired[
        "aws_sdk_directory_service.types.certificate_registered_date_time.CertificateRegisteredDateTime"
    ]
    """<p>The date and time that the certificate was registered.</p>"""
    expiry_date_time: NotRequired[
        "aws_sdk_directory_service.types.certificate_expiry_date_time.CertificateExpiryDateTime"
    ]
    """<p>The date and time when the certificate will expire.</p>"""
    type: NotRequired[
        "aws_sdk_directory_service.types.certificate_type.CertificateType"
    ]
    """<p>The function that the registered certificate performs. Valid values include <code>ClientLDAPS</code> or <code>ClientCertAuth</code>. The default value is <code>ClientLDAPS</code>.</p>"""
    client_cert_auth_settings: NotRequired[
        "aws_sdk_directory_service.types.client_cert_auth_settings.ClientCertAuthSettings"
    ]
    """<p>A <code>ClientCertAuthSettings</code> object that contains client certificate authentication settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Certificate) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    if "state" in value:
        import aws_sdk_directory_service.types.certificate_state

        out["State"] = (
            aws_sdk_directory_service.types.certificate_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "common_name" in value:
        out["CommonName"] = value["common_name"]
    if "registered_date_time" in value:
        import aws_sdk_directory_service.types.certificate_registered_date_time

        out["RegisteredDateTime"] = (
            aws_sdk_directory_service.types.certificate_registered_date_time.serialize_aws_json_1_1(
                value["registered_date_time"]
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
    if "client_cert_auth_settings" in value:
        import aws_sdk_directory_service.types.client_cert_auth_settings

        out["ClientCertAuthSettings"] = (
            aws_sdk_directory_service.types.client_cert_auth_settings.serialize_aws_json_1_1(
                value["client_cert_auth_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    if "State" in data:
        import aws_sdk_directory_service.types.certificate_state

        out["state"] = (
            aws_sdk_directory_service.types.certificate_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "CommonName" in data:
        out["common_name"] = data["CommonName"]
    if "RegisteredDateTime" in data:
        import aws_sdk_directory_service.types.certificate_registered_date_time

        out["registered_date_time"] = (
            aws_sdk_directory_service.types.certificate_registered_date_time.deserialize_aws_json_1_1(
                data["RegisteredDateTime"]
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
    if "ClientCertAuthSettings" in data:
        import aws_sdk_directory_service.types.client_cert_auth_settings

        out["client_cert_auth_settings"] = (
            aws_sdk_directory_service.types.client_cert_auth_settings.deserialize_aws_json_1_1(
                data["ClientCertAuthSettings"]
            )
        )
    return out
