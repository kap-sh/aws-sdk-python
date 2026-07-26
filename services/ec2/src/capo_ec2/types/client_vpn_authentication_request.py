"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthenticationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.certificate_authentication_request
    import capo_ec2.types.client_vpn_authentication_type
    import capo_ec2.types.directory_service_authentication_request
    import capo_ec2.types.federated_authentication_request


class ClientVpnAuthenticationRequest(TypedDict, closed=True):
    type: NotRequired[
        "capo_ec2.types.client_vpn_authentication_type.ClientVpnAuthenticationType"
    ]
    """<p>The type of client authentication to be used.</p>"""
    active_directory: NotRequired[
        "capo_ec2.types.directory_service_authentication_request.DirectoryServiceAuthenticationRequest"
    ]
    """<p>Information about the Active Directory to be used, if applicable. You must provide this information if <b>Type</b> is <code>directory-service-authentication</code>.</p>"""
    mutual_authentication: NotRequired[
        "capo_ec2.types.certificate_authentication_request.CertificateAuthenticationRequest"
    ]
    """<p>Information about the authentication certificates to be used, if applicable. You must provide this information if <b>Type</b> is <code>certificate-authentication</code>.</p>"""
    federated_authentication: NotRequired[
        "capo_ec2.types.federated_authentication_request.FederatedAuthenticationRequest"
    ]
    """<p>Information about the IAM SAML identity provider to be used, if applicable. You must provide this information if <b>Type</b> is <code>federated-authentication</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnAuthenticationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import capo_ec2.types.client_vpn_authentication_type

        capo_ec2.types.client_vpn_authentication_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "active_directory" in value:
        import capo_ec2.types.directory_service_authentication_request

        capo_ec2.types.directory_service_authentication_request.serialize_ec2_query(
            value["active_directory"], pairs, f"{prefix}.ActiveDirectory"
        )
    if "mutual_authentication" in value:
        import capo_ec2.types.certificate_authentication_request

        capo_ec2.types.certificate_authentication_request.serialize_ec2_query(
            value["mutual_authentication"], pairs, f"{prefix}.MutualAuthentication"
        )
    if "federated_authentication" in value:
        import capo_ec2.types.federated_authentication_request

        capo_ec2.types.federated_authentication_request.serialize_ec2_query(
            value["federated_authentication"],
            pairs,
            f"{prefix}.FederatedAuthentication",
        )


def deserialize_ec2_query(el: Element) -> ClientVpnAuthenticationRequest:
    out: ClientVpnAuthenticationRequest = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_ec2.types.client_vpn_authentication_type

        out["type"] = (
            capo_ec2.types.client_vpn_authentication_type.deserialize_ec2_query(
                child_type
            )
        )
    child_active_directory = el.find("ActiveDirectory")
    if child_active_directory is not None:
        import capo_ec2.types.directory_service_authentication_request

        out["active_directory"] = (
            capo_ec2.types.directory_service_authentication_request.deserialize_ec2_query(
                child_active_directory
            )
        )
    child_mutual_authentication = el.find("MutualAuthentication")
    if child_mutual_authentication is not None:
        import capo_ec2.types.certificate_authentication_request

        out["mutual_authentication"] = (
            capo_ec2.types.certificate_authentication_request.deserialize_ec2_query(
                child_mutual_authentication
            )
        )
    child_federated_authentication = el.find("FederatedAuthentication")
    if child_federated_authentication is not None:
        import capo_ec2.types.federated_authentication_request

        out["federated_authentication"] = (
            capo_ec2.types.federated_authentication_request.deserialize_ec2_query(
                child_federated_authentication
            )
        )
    return out
