"""Generated from Smithy shape ``com.amazonaws.ram#ListSourceAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.associated_source_list
    import capo_ram.types.string


class ListSourceAssociationsResponse(TypedDict, closed=True):
    source_associations: NotRequired[
        "capo_ram.types.associated_source_list.AssociatedSourceList"
    ]
    """<p>Information about the source associations.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceAssociationsResponse) -> dict:
    out: dict = {}
    if "source_associations" in value:
        import capo_ram.types.associated_source_list

        out["sourceAssociations"] = (
            capo_ram.types.associated_source_list.serialize_json(
                value["source_associations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSourceAssociationsResponse:
    out: ListSourceAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "sourceAssociations" in data:
        import capo_ram.types.associated_source_list

        out["source_associations"] = (
            capo_ram.types.associated_source_list.deserialize_json(
                data["sourceAssociations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
