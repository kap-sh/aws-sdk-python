"""Generated from Smithy shape ``com.amazonaws.iot#ListThingTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.thing_type_list


class ListThingTypesResponse(TypedDict, closed=True):
    thing_types: NotRequired["capo_iot.types.thing_type_list.ThingTypeList"]
    """<p>The thing types.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results. Will not be returned if operation has returned all results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingTypesResponse) -> dict:
    out: dict = {}
    if "thing_types" in value:
        import capo_iot.types.thing_type_list

        out["thingTypes"] = capo_iot.types.thing_type_list.serialize_json(
            value["thing_types"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingTypesResponse:
    out: ListThingTypesResponse = {}  # type: ignore[typeddict-item]
    if "thingTypes" in data:
        import capo_iot.types.thing_type_list

        out["thing_types"] = capo_iot.types.thing_type_list.deserialize_json(
            data["thingTypes"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
