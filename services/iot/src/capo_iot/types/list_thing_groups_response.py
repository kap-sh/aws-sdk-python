"""Generated from Smithy shape ``com.amazonaws.iot#ListThingGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.thing_group_name_and_arn_list


class ListThingGroupsResponse(TypedDict, closed=True):
    thing_groups: NotRequired[
        "capo_iot.types.thing_group_name_and_arn_list.ThingGroupNameAndArnList"
    ]
    """<p>The thing groups.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results. Will not be returned if operation has returned all results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingGroupsResponse) -> dict:
    out: dict = {}
    if "thing_groups" in value:
        import capo_iot.types.thing_group_name_and_arn_list

        out["thingGroups"] = (
            capo_iot.types.thing_group_name_and_arn_list.serialize_json(
                value["thing_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingGroupsResponse:
    out: ListThingGroupsResponse = {}  # type: ignore[typeddict-item]
    if "thingGroups" in data:
        import capo_iot.types.thing_group_name_and_arn_list

        out["thing_groups"] = (
            capo_iot.types.thing_group_name_and_arn_list.deserialize_json(
                data["thingGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
