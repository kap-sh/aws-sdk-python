"""Generated from Smithy shape ``com.amazonaws.iot#ListThingsInThingGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.thing_name_list


class ListThingsInThingGroupResponse(TypedDict):
    things: NotRequired["aws_sdk_iot.types.thing_name_list.ThingNameList"]
    """<p>The things in the specified thing group.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingsInThingGroupResponse) -> dict:
    out: dict = {}
    if "things" in value:
        import aws_sdk_iot.types.thing_name_list

        out["things"] = aws_sdk_iot.types.thing_name_list.serialize_json(
            value["things"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingsInThingGroupResponse:
    out: ListThingsInThingGroupResponse = {}  # type: ignore[typeddict-item]
    if "things" in data:
        import aws_sdk_iot.types.thing_name_list

        out["things"] = aws_sdk_iot.types.thing_name_list.deserialize_json(
            data["things"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
