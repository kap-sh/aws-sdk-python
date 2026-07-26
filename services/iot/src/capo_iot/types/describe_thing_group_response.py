"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.dynamic_group_status
    import capo_iot.types.index_name
    import capo_iot.types.query_string
    import capo_iot.types.query_version
    import capo_iot.types.thing_group_arn
    import capo_iot.types.thing_group_id
    import capo_iot.types.thing_group_metadata
    import capo_iot.types.thing_group_name
    import capo_iot.types.thing_group_properties
    import capo_iot.types.version


class DescribeThingGroupResponse(TypedDict, closed=True):
    thing_group_name: NotRequired["capo_iot.types.thing_group_name.ThingGroupName"]
    """<p>The name of the thing group.</p>"""
    thing_group_id: NotRequired["capo_iot.types.thing_group_id.ThingGroupId"]
    """<p>The thing group ID.</p>"""
    thing_group_arn: NotRequired["capo_iot.types.thing_group_arn.ThingGroupArn"]
    """<p>The thing group ARN.</p>"""
    version: "capo_iot.types.version.Version"
    """<p>The version of the thing group.</p>"""
    thing_group_properties: NotRequired[
        "capo_iot.types.thing_group_properties.ThingGroupProperties"
    ]
    """<p>The thing group properties.</p>"""
    thing_group_metadata: NotRequired[
        "capo_iot.types.thing_group_metadata.ThingGroupMetadata"
    ]
    """<p>Thing group metadata.</p>"""
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The dynamic thing group index name.</p>"""
    query_string: NotRequired["capo_iot.types.query_string.QueryString"]
    """<p>The dynamic thing group search query string.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The dynamic thing group query version.</p>"""
    status: NotRequired["capo_iot.types.dynamic_group_status.DynamicGroupStatus"]
    """<p>The dynamic thing group status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingGroupResponse) -> dict:
    out: dict = {}
    if "thing_group_name" in value:
        out["thingGroupName"] = value["thing_group_name"]
    if "thing_group_id" in value:
        out["thingGroupId"] = value["thing_group_id"]
    if "thing_group_arn" in value:
        out["thingGroupArn"] = value["thing_group_arn"]
    out["version"] = value.get("version", 0)
    if "thing_group_properties" in value:
        import capo_iot.types.thing_group_properties

        out["thingGroupProperties"] = (
            capo_iot.types.thing_group_properties.serialize_json(
                value["thing_group_properties"]
            )
        )
    if "thing_group_metadata" in value:
        import capo_iot.types.thing_group_metadata

        out["thingGroupMetadata"] = capo_iot.types.thing_group_metadata.serialize_json(
            value["thing_group_metadata"]
        )
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    if "status" in value:
        import capo_iot.types.dynamic_group_status

        out["status"] = capo_iot.types.dynamic_group_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> DescribeThingGroupResponse:
    out: DescribeThingGroupResponse = {}  # type: ignore[typeddict-item]
    if "thingGroupName" in data:
        out["thing_group_name"] = data["thingGroupName"]
    if "thingGroupId" in data:
        out["thing_group_id"] = data["thingGroupId"]
    if "thingGroupArn" in data:
        out["thing_group_arn"] = data["thingGroupArn"]
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if "thingGroupProperties" in data:
        import capo_iot.types.thing_group_properties

        out["thing_group_properties"] = (
            capo_iot.types.thing_group_properties.deserialize_json(
                data["thingGroupProperties"]
            )
        )
    if "thingGroupMetadata" in data:
        import capo_iot.types.thing_group_metadata

        out["thing_group_metadata"] = (
            capo_iot.types.thing_group_metadata.deserialize_json(
                data["thingGroupMetadata"]
            )
        )
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "queryVersion" in data:
        out["query_version"] = data["queryVersion"]
    if "status" in data:
        import capo_iot.types.dynamic_group_status

        out["status"] = capo_iot.types.dynamic_group_status.deserialize_json(
            data["status"]
        )
    return out
