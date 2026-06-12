"""Generated from Smithy shape ``com.amazonaws.workmail#ListAliasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.aliases
    import aws_sdk_workmail.types.next_token


class ListAliasesResponse(TypedDict):
    aliases: NotRequired["aws_sdk_workmail.types.aliases.Aliases"]
    """<p>The entity's paginated aliases.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The value is \"null\" when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesResponse) -> dict:
    out: dict = {}
    if "aliases" in value:
        import aws_sdk_workmail.types.aliases

        out["Aliases"] = aws_sdk_workmail.types.aliases.serialize_aws_json_1_1(
            value["aliases"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesResponse:
    out: ListAliasesResponse = {}  # type: ignore[typeddict-item]
    if "Aliases" in data:
        import aws_sdk_workmail.types.aliases

        out["aliases"] = aws_sdk_workmail.types.aliases.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
