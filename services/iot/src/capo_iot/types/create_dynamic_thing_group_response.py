"""Generated from Smithy shape ``com.amazonaws.iot#CreateDynamicThingGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.index_name
    import capo_iot.types.query_string
    import capo_iot.types.query_version
    import capo_iot.types.thing_group_arn
    import capo_iot.types.thing_group_id
    import capo_iot.types.thing_group_name


class CreateDynamicThingGroupResponse(TypedDict, closed=True):
    thing_group_name: NotRequired["capo_iot.types.thing_group_name.ThingGroupName"]
    """<p>The dynamic thing group name.</p>"""
    thing_group_arn: NotRequired["capo_iot.types.thing_group_arn.ThingGroupArn"]
    """<p>The dynamic thing group ARN.</p>"""
    thing_group_id: NotRequired["capo_iot.types.thing_group_id.ThingGroupId"]
    """<p>The dynamic thing group ID.</p>"""
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The dynamic thing group index name.</p>"""
    query_string: NotRequired["capo_iot.types.query_string.QueryString"]
    """<p>The dynamic thing group search query string.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The dynamic thing group query version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDynamicThingGroupResponse) -> dict:
    out: dict = {}
    if "thing_group_name" in value:
        out["thingGroupName"] = value["thing_group_name"]
    if "thing_group_arn" in value:
        out["thingGroupArn"] = value["thing_group_arn"]
    if "thing_group_id" in value:
        out["thingGroupId"] = value["thing_group_id"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    return out


def deserialize_json(data: dict) -> CreateDynamicThingGroupResponse:
    out: CreateDynamicThingGroupResponse = {}  # type: ignore[typeddict-item]
    if "thingGroupName" in data:
        out["thing_group_name"] = data["thingGroupName"]
    if "thingGroupArn" in data:
        out["thing_group_arn"] = data["thingGroupArn"]
    if "thingGroupId" in data:
        out["thing_group_id"] = data["thingGroupId"]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "queryVersion" in data:
        out["query_version"] = data["queryVersion"]
    return out
