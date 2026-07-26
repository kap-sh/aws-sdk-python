"""Generated from Smithy shape ``com.amazonaws.directoryservice#EnableClientAuthenticationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.client_authentication_type
    import capo_directory_service.types.directory_id


class EnableClientAuthenticationRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the specified directory. </p>"""
    type: "capo_directory_service.types.client_authentication_type.ClientAuthenticationType"
    """<p>The type of client authentication to enable. Currently only the value <code>SmartCard</code> is supported. Smart card authentication in AD Connector requires that you enable Kerberos Constrained Delegation for the Service User to the LDAP service in your self-managed AD. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableClientAuthenticationRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_directory_service.types.client_authentication_type

    out["Type"] = (
        capo_directory_service.types.client_authentication_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableClientAuthenticationRequest:
    out: EnableClientAuthenticationRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError(
            "EnableClientAuthenticationRequest.directory_id required"
        )
    if "Type" in data:
        import capo_directory_service.types.client_authentication_type

        out["type"] = (
            capo_directory_service.types.client_authentication_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("EnableClientAuthenticationRequest.type required")
    return out
