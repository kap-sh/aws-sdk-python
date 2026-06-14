"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeConnectionAliasesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connection_alias_list
    import aws_sdk_workspaces.types.pagination_token


class DescribeConnectionAliasesResult(TypedDict):
    connection_aliases: NotRequired[
        "aws_sdk_workspaces.types.connection_alias_list.ConnectionAliasList"
    ]
    """<p>Information about the specified connection aliases.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionAliasesResult) -> dict:
    out: dict = {}
    if "connection_aliases" in value:
        import aws_sdk_workspaces.types.connection_alias_list

        out["ConnectionAliases"] = (
            aws_sdk_workspaces.types.connection_alias_list.serialize_aws_json_1_1(
                value["connection_aliases"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionAliasesResult:
    out: DescribeConnectionAliasesResult = {}  # type: ignore[typeddict-item]
    if "ConnectionAliases" in data:
        import aws_sdk_workspaces.types.connection_alias_list

        out["connection_aliases"] = (
            aws_sdk_workspaces.types.connection_alias_list.deserialize_aws_json_1_1(
                data["ConnectionAliases"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
