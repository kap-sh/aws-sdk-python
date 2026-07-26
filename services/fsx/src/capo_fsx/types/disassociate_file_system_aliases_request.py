"""Generated from Smithy shape ``com.amazonaws.fsx#DisassociateFileSystemAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.alternate_dns_names
    import capo_fsx.types.client_request_token
    import capo_fsx.types.file_system_id


class DisassociateFileSystemAliasesRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    """<p>Specifies the file system from which to disassociate the DNS aliases.</p>"""
    aliases: NotRequired["capo_fsx.types.alternate_dns_names.AlternateDNSNames"]
    """<p>An array of one or more DNS alias names to disassociate, or remove, from the file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFileSystemAliasesRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "aliases" in value:
        import capo_fsx.types.alternate_dns_names

        out["Aliases"] = capo_fsx.types.alternate_dns_names.serialize_aws_json_1_1(
            value["aliases"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFileSystemAliasesRequest:
    out: DisassociateFileSystemAliasesRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "Aliases" in data:
        import capo_fsx.types.alternate_dns_names

        out["aliases"] = capo_fsx.types.alternate_dns_names.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    return out
