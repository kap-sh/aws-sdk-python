"""Generated from Smithy shape ``com.amazonaws.iot#ListThingsInThingGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.thing_name_list


class ListThingsInThingGroupResponse(TypedDict, closed=True):
    things: NotRequired["capo_iot.types.thing_name_list.ThingNameList"]
    """<p>The things in the specified thing group.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingsInThingGroupResponse) -> dict:
    out: dict = {}
    if "things" in value:
        import capo_iot.types.thing_name_list

        out["things"] = capo_iot.types.thing_name_list.serialize_json(value["things"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingsInThingGroupResponse:
    out: ListThingsInThingGroupResponse = {}  # type: ignore[typeddict-item]
    if "things" in data:
        import capo_iot.types.thing_name_list

        out["things"] = capo_iot.types.thing_name_list.deserialize_json(data["things"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
