"""Generated from Smithy shape ``com.amazonaws.appstream#CreateDirectoryConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.certificate_based_auth_properties
    import aws_sdk_appstream.types.directory_name
    import aws_sdk_appstream.types.organizational_unit_distinguished_names_list
    import aws_sdk_appstream.types.service_account_credentials


class CreateDirectoryConfigRequest(TypedDict):
    directory_name: NotRequired["aws_sdk_appstream.types.directory_name.DirectoryName"]
    """<p>The fully qualified name of the directory (for example, corp.example.com).</p>"""
    organizational_unit_distinguished_names: NotRequired[
        "aws_sdk_appstream.types.organizational_unit_distinguished_names_list.OrganizationalUnitDistinguishedNamesList"
    ]
    """<p>The distinguished names of the organizational units for computer accounts.</p>"""
    service_account_credentials: NotRequired[
        "aws_sdk_appstream.types.service_account_credentials.ServiceAccountCredentials"
    ]
    """<p>The credentials for the service account used by the fleet or image builder to connect to the directory.</p>"""
    certificate_based_auth_properties: NotRequired[
        "aws_sdk_appstream.types.certificate_based_auth_properties.CertificateBasedAuthProperties"
    ]
    """<p>The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances. Fallback is turned on by default when certificate-based authentication is <b>Enabled</b> . Fallback allows users to log in using their AD domain password if certificate-based authentication is unsuccessful, or to unlock a desktop lock screen. <b>Enabled_no_directory_login_fallback</b> enables certificate-based authentication, but does not allow users to log in using their AD domain password. Users will be disconnected to re-authenticate using certificates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDirectoryConfigRequest) -> dict:
    out: dict = {}
    if "directory_name" in value:
        out["DirectoryName"] = value["directory_name"]
    if "organizational_unit_distinguished_names" in value:
        import aws_sdk_appstream.types.organizational_unit_distinguished_names_list

        out["OrganizationalUnitDistinguishedNames"] = (
            aws_sdk_appstream.types.organizational_unit_distinguished_names_list.serialize_aws_json_1_1(
                value["organizational_unit_distinguished_names"]
            )
        )
    if "service_account_credentials" in value:
        import aws_sdk_appstream.types.service_account_credentials

        out["ServiceAccountCredentials"] = (
            aws_sdk_appstream.types.service_account_credentials.serialize_aws_json_1_1(
                value["service_account_credentials"]
            )
        )
    if "certificate_based_auth_properties" in value:
        import aws_sdk_appstream.types.certificate_based_auth_properties

        out["CertificateBasedAuthProperties"] = (
            aws_sdk_appstream.types.certificate_based_auth_properties.serialize_aws_json_1_1(
                value["certificate_based_auth_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDirectoryConfigRequest:
    out: CreateDirectoryConfigRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryName" in data:
        out["directory_name"] = data["DirectoryName"]
    if "OrganizationalUnitDistinguishedNames" in data:
        import aws_sdk_appstream.types.organizational_unit_distinguished_names_list

        out["organizational_unit_distinguished_names"] = (
            aws_sdk_appstream.types.organizational_unit_distinguished_names_list.deserialize_aws_json_1_1(
                data["OrganizationalUnitDistinguishedNames"]
            )
        )
    if "ServiceAccountCredentials" in data:
        import aws_sdk_appstream.types.service_account_credentials

        out["service_account_credentials"] = (
            aws_sdk_appstream.types.service_account_credentials.deserialize_aws_json_1_1(
                data["ServiceAccountCredentials"]
            )
        )
    if "CertificateBasedAuthProperties" in data:
        import aws_sdk_appstream.types.certificate_based_auth_properties

        out["certificate_based_auth_properties"] = (
            aws_sdk_appstream.types.certificate_based_auth_properties.deserialize_aws_json_1_1(
                data["CertificateBasedAuthProperties"]
            )
        )
    return out
