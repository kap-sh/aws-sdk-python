"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeFileSystemAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.aliases
    import aws_sdk_fsx.types.next_token


class DescribeFileSystemAliasesResponse(TypedDict, closed=True):
    aliases: NotRequired["aws_sdk_fsx.types.aliases.Aliases"]
    """<p>An array of one or more DNS aliases currently associated with the specified file system.</p>"""
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]
    """<p>Present if there are more DNS aliases than returned in the response (String). You can use the <code>NextToken</code> value in a later request to fetch additional descriptions. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileSystemAliasesResponse) -> dict:
    out: dict = {}
    if "aliases" in value:
        import aws_sdk_fsx.types.aliases

        out["Aliases"] = aws_sdk_fsx.types.aliases.serialize_aws_json_1_1(
            value["aliases"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileSystemAliasesResponse:
    out: DescribeFileSystemAliasesResponse = {}  # type: ignore[typeddict-item]
    if "Aliases" in data:
        import aws_sdk_fsx.types.aliases

        out["aliases"] = aws_sdk_fsx.types.aliases.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
