"""Generated from Smithy shape ``com.amazonaws.iot#SearchIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.thing_document_list
    import capo_iot.types.thing_group_document_list


class SearchIndexResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token used to get the next set of results, or <code>null</code> if there are no additional results.</p>"""
    things: NotRequired["capo_iot.types.thing_document_list.ThingDocumentList"]
    """<p>The things that match the search query.</p>"""
    thing_groups: NotRequired[
        "capo_iot.types.thing_group_document_list.ThingGroupDocumentList"
    ]
    """<p>The thing groups that match the search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchIndexResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "things" in value:
        import capo_iot.types.thing_document_list

        out["things"] = capo_iot.types.thing_document_list.serialize_json(
            value["things"]
        )
    if "thing_groups" in value:
        import capo_iot.types.thing_group_document_list

        out["thingGroups"] = capo_iot.types.thing_group_document_list.serialize_json(
            value["thing_groups"]
        )
    return out


def deserialize_json(data: dict) -> SearchIndexResponse:
    out: SearchIndexResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "things" in data:
        import capo_iot.types.thing_document_list

        out["things"] = capo_iot.types.thing_document_list.deserialize_json(
            data["things"]
        )
    if "thingGroups" in data:
        import capo_iot.types.thing_group_document_list

        out["thing_groups"] = capo_iot.types.thing_group_document_list.deserialize_json(
            data["thingGroups"]
        )
    return out
