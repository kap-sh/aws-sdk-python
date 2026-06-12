"""Generated from Smithy shape ``com.amazonaws.fsx#DisassociateFileSystemAliasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.aliases


class DisassociateFileSystemAliasesResponse(TypedDict):
    aliases: NotRequired["aws_sdk_fsx.types.aliases.Aliases"]
    """<p>An array of one or more DNS aliases that Amazon FSx is attempting to disassociate from the file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFileSystemAliasesResponse) -> dict:
    out: dict = {}
    if "aliases" in value:
        import aws_sdk_fsx.types.aliases

        out["Aliases"] = aws_sdk_fsx.types.aliases.serialize_aws_json_1_1(
            value["aliases"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFileSystemAliasesResponse:
    out: DisassociateFileSystemAliasesResponse = {}  # type: ignore[typeddict-item]
    if "Aliases" in data:
        import aws_sdk_fsx.types.aliases

        out["aliases"] = aws_sdk_fsx.types.aliases.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    return out
