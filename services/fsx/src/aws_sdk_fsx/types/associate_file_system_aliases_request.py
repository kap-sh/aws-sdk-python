"""Generated from Smithy shape ``com.amazonaws.fsx#AssociateFileSystemAliasesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.alternate_dns_names
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.file_system_id


class AssociateFileSystemAliasesRequest(TypedDict):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]
    """<p>Specifies the file system with which you want to associate one or more DNS aliases.</p>"""
    aliases: NotRequired["aws_sdk_fsx.types.alternate_dns_names.AlternateDNSNames"]
    """<p>An array of one or more DNS alias names to associate with the file system. The alias name has to comply with the following formatting requirements:</p> <ul> <li> <p>Formatted as a fully-qualified domain name (FQDN), <i> <code>hostname.domain</code> </i>, for example, <code>accounting.corp.example.com</code>.</p> </li> <li> <p>Can contain alphanumeric characters and the hyphen (-).</p> </li> <li> <p>Cannot start or end with a hyphen.</p> </li> <li> <p>Can start with a numeric.</p> </li> </ul> <p>For DNS alias names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateFileSystemAliasesRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "aliases" in value:
        import aws_sdk_fsx.types.alternate_dns_names

        out["Aliases"] = aws_sdk_fsx.types.alternate_dns_names.serialize_aws_json_1_1(
            value["aliases"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateFileSystemAliasesRequest:
    out: AssociateFileSystemAliasesRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "Aliases" in data:
        import aws_sdk_fsx.types.alternate_dns_names

        out["aliases"] = aws_sdk_fsx.types.alternate_dns_names.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    return out
