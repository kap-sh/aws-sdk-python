"""Generated from Smithy shape ``com.amazonaws.lambda#ListAliasesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.alias_list
    import aws_sdk_lambda.types.string


class ListAliasesResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""
    aliases: NotRequired["aws_sdk_lambda.types.alias_list.AliasList"]
    """<p>A list of aliases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAliasesResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "aliases" in value:
        import aws_sdk_lambda.types.alias_list

        out["Aliases"] = aws_sdk_lambda.types.alias_list.serialize_json(
            value["aliases"]
        )
    return out


def deserialize_json(data: dict) -> ListAliasesResponse:
    out: ListAliasesResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Aliases" in data:
        import aws_sdk_lambda.types.alias_list

        out["aliases"] = aws_sdk_lambda.types.alias_list.deserialize_json(
            data["Aliases"]
        )
    return out
