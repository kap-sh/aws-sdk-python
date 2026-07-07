"""Generated from Smithy shape ``com.amazonaws.iot#ListThingGroupsForThingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.thing_group_name_and_arn_list


class ListThingGroupsForThingResponse(TypedDict, closed=True):
    thing_groups: NotRequired[
        "aws_sdk_iot.types.thing_group_name_and_arn_list.ThingGroupNameAndArnList"
    ]
    """<p>The thing groups.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingGroupsForThingResponse) -> dict:
    out: dict = {}
    if "thing_groups" in value:
        import aws_sdk_iot.types.thing_group_name_and_arn_list

        out["thingGroups"] = (
            aws_sdk_iot.types.thing_group_name_and_arn_list.serialize_json(
                value["thing_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingGroupsForThingResponse:
    out: ListThingGroupsForThingResponse = {}  # type: ignore[typeddict-item]
    if "thingGroups" in data:
        import aws_sdk_iot.types.thing_group_name_and_arn_list

        out["thing_groups"] = (
            aws_sdk_iot.types.thing_group_name_and_arn_list.deserialize_json(
                data["thingGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
