"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegisterCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.certificate_data
    import aws_sdk_directory_service.types.certificate_type
    import aws_sdk_directory_service.types.client_cert_auth_settings
    import aws_sdk_directory_service.types.directory_id


class RegisterCertificateRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    certificate_data: "aws_sdk_directory_service.types.certificate_data.CertificateData"
    """<p>The certificate PEM string that needs to be registered.</p>"""
    type: NotRequired[
        "aws_sdk_directory_service.types.certificate_type.CertificateType"
    ]
    """<p>The function that the registered certificate performs. Valid values include <code>ClientLDAPS</code> or <code>ClientCertAuth</code>. The default value is <code>ClientLDAPS</code>.</p>"""
    client_cert_auth_settings: NotRequired[
        "aws_sdk_directory_service.types.client_cert_auth_settings.ClientCertAuthSettings"
    ]
    """<p>A <code>ClientCertAuthSettings</code> object that contains client certificate authentication settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterCertificateRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["CertificateData"] = value["certificate_data"]
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


def deserialize_aws_json_1_1(data: dict) -> RegisterCertificateRequest:
    out: RegisterCertificateRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("RegisterCertificateRequest.directory_id required")
    if "CertificateData" in data:
        out["certificate_data"] = data["CertificateData"]
    else:
        raise DeserializationError(
            "RegisterCertificateRequest.certificate_data required"
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
