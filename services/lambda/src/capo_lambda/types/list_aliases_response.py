"""Generated from Smithy shape ``com.amazonaws.lambda#ListAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.alias_list
    import capo_lambda.types.string


class ListAliasesResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""
    aliases: NotRequired["capo_lambda.types.alias_list.AliasList"]
    """<p>A list of aliases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAliasesResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "aliases" in value:
        import capo_lambda.types.alias_list

        out["Aliases"] = capo_lambda.types.alias_list.serialize_json(value["aliases"])
    return out


def deserialize_json(data: dict) -> ListAliasesResponse:
    out: ListAliasesResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Aliases" in data:
        import capo_lambda.types.alias_list

        out["aliases"] = capo_lambda.types.alias_list.deserialize_json(data["Aliases"])
    return out
