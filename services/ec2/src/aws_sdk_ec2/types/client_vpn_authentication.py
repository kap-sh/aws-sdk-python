"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthentication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.certificate_authentication
    import aws_sdk_ec2.types.client_vpn_authentication_type
    import aws_sdk_ec2.types.directory_service_authentication
    import aws_sdk_ec2.types.federated_authentication


class ClientVpnAuthentication(TypedDict):
    type: NotRequired[
        "aws_sdk_ec2.types.client_vpn_authentication_type.ClientVpnAuthenticationType"
    ]
    """<p>The authentication type used.</p>"""
    active_directory: NotRequired[
        "aws_sdk_ec2.types.directory_service_authentication.DirectoryServiceAuthentication"
    ]
    """<p>Information about the Active Directory, if applicable.</p>"""
    mutual_authentication: NotRequired[
        "aws_sdk_ec2.types.certificate_authentication.CertificateAuthentication"
    ]
    """<p>Information about the authentication certificates, if applicable.</p>"""
    federated_authentication: NotRequired[
        "aws_sdk_ec2.types.federated_authentication.FederatedAuthentication"
    ]
    """<p>Information about the IAM SAML identity provider, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnAuthentication, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import aws_sdk_ec2.types.client_vpn_authentication_type

        aws_sdk_ec2.types.client_vpn_authentication_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "active_directory" in value:
        import aws_sdk_ec2.types.directory_service_authentication

        aws_sdk_ec2.types.directory_service_authentication.serialize_ec2_query(
            value["active_directory"], pairs, f"{prefix}.ActiveDirectory"
        )
    if "mutual_authentication" in value:
        import aws_sdk_ec2.types.certificate_authentication

        aws_sdk_ec2.types.certificate_authentication.serialize_ec2_query(
            value["mutual_authentication"], pairs, f"{prefix}.MutualAuthentication"
        )
    if "federated_authentication" in value:
        import aws_sdk_ec2.types.federated_authentication

        aws_sdk_ec2.types.federated_authentication.serialize_ec2_query(
            value["federated_authentication"],
            pairs,
            f"{prefix}.FederatedAuthentication",
        )


def deserialize_ec2_query(el: Element) -> ClientVpnAuthentication:
    out: ClientVpnAuthentication = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.client_vpn_authentication_type

        out["type"] = (
            aws_sdk_ec2.types.client_vpn_authentication_type.deserialize_ec2_query(
                child_type
            )
        )
    child_active_directory = el.find("ActiveDirectory")
    if child_active_directory is not None:
        import aws_sdk_ec2.types.directory_service_authentication

        out["active_directory"] = (
            aws_sdk_ec2.types.directory_service_authentication.deserialize_ec2_query(
                child_active_directory
            )
        )
    child_mutual_authentication = el.find("MutualAuthentication")
    if child_mutual_authentication is not None:
        import aws_sdk_ec2.types.certificate_authentication

        out["mutual_authentication"] = (
            aws_sdk_ec2.types.certificate_authentication.deserialize_ec2_query(
                child_mutual_authentication
            )
        )
    child_federated_authentication = el.find("FederatedAuthentication")
    if child_federated_authentication is not None:
        import aws_sdk_ec2.types.federated_authentication

        out["federated_authentication"] = (
            aws_sdk_ec2.types.federated_authentication.deserialize_ec2_query(
                child_federated_authentication
            )
        )
    return out
