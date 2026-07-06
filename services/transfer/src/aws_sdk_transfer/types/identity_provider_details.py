"""Generated from Smithy shape ``com.amazonaws.transfer#IdentityProviderDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.directory_id
    import aws_sdk_transfer.types.function
    import aws_sdk_transfer.types.role
    import aws_sdk_transfer.types.sftp_authentication_methods
    import aws_sdk_transfer.types.url


class IdentityProviderDetails(TypedDict, closed=True):
    url: NotRequired["aws_sdk_transfer.types.url.Url"]
    """<p>Provides the location of the service endpoint used to authenticate users.</p>"""
    invocation_role: NotRequired["aws_sdk_transfer.types.role.Role"]
    """<p>This parameter is only applicable if your <code>IdentityProviderType</code> is <code>API_GATEWAY</code>. Provides the type of <code>InvocationRole</code> used to authenticate the user account.</p>"""
    directory_id: NotRequired["aws_sdk_transfer.types.directory_id.DirectoryId"]
    """<p>The identifier of the Directory Service directory that you want to use as your identity provider.</p>"""
    function: NotRequired["aws_sdk_transfer.types.function.Function"]
    """<p>The ARN for a Lambda function to use for the Identity provider.</p>"""
    sftp_authentication_methods: NotRequired[
        "aws_sdk_transfer.types.sftp_authentication_methods.SftpAuthenticationMethods"
    ]
    """<p>For SFTP-enabled servers, and for custom identity providers <i>only</i>, you can specify whether to authenticate using a password, SSH key pair, or both.</p> <ul> <li> <p> <code>PASSWORD</code> - users must provide their password to connect.</p> </li> <li> <p> <code>PUBLIC_KEY</code> - users must provide their private key to connect.</p> </li> <li> <p> <code>PUBLIC_KEY_OR_PASSWORD</code> - users can authenticate with either their password or their key. This is the default value.</p> </li> <li> <p> <code>PUBLIC_KEY_AND_PASSWORD</code> - users must provide both their private key and their password to connect. The server checks the key first, and then if the key is valid, the system prompts for a password. If the private key provided does not match the public key that is stored, authentication fails.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityProviderDetails) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "invocation_role" in value:
        out["InvocationRole"] = value["invocation_role"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "function" in value:
        out["Function"] = value["function"]
    if "sftp_authentication_methods" in value:
        import aws_sdk_transfer.types.sftp_authentication_methods

        out["SftpAuthenticationMethods"] = (
            aws_sdk_transfer.types.sftp_authentication_methods.serialize_aws_json_1_1(
                value["sftp_authentication_methods"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityProviderDetails:
    out: IdentityProviderDetails = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    if "InvocationRole" in data:
        out["invocation_role"] = data["InvocationRole"]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Function" in data:
        out["function"] = data["Function"]
    if "SftpAuthenticationMethods" in data:
        import aws_sdk_transfer.types.sftp_authentication_methods

        out["sftp_authentication_methods"] = (
            aws_sdk_transfer.types.sftp_authentication_methods.deserialize_aws_json_1_1(
                data["SftpAuthenticationMethods"]
            )
        )
    return out
