"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.dynamic_group_status
    import aws_sdk_iot.types.index_name
    import aws_sdk_iot.types.query_string
    import aws_sdk_iot.types.query_version
    import aws_sdk_iot.types.thing_group_arn
    import aws_sdk_iot.types.thing_group_id
    import aws_sdk_iot.types.thing_group_metadata
    import aws_sdk_iot.types.thing_group_name
    import aws_sdk_iot.types.thing_group_properties
    import aws_sdk_iot.types.version


class DescribeThingGroupResponse(TypedDict):
    thing_group_name: NotRequired["aws_sdk_iot.types.thing_group_name.ThingGroupName"]
    """<p>The name of the thing group.</p>"""
    thing_group_id: NotRequired["aws_sdk_iot.types.thing_group_id.ThingGroupId"]
    """<p>The thing group ID.</p>"""
    thing_group_arn: NotRequired["aws_sdk_iot.types.thing_group_arn.ThingGroupArn"]
    """<p>The thing group ARN.</p>"""
    version: "aws_sdk_iot.types.version.Version"
    """<p>The version of the thing group.</p>"""
    thing_group_properties: NotRequired[
        "aws_sdk_iot.types.thing_group_properties.ThingGroupProperties"
    ]
    """<p>The thing group properties.</p>"""
    thing_group_metadata: NotRequired[
        "aws_sdk_iot.types.thing_group_metadata.ThingGroupMetadata"
    ]
    """<p>Thing group metadata.</p>"""
    index_name: NotRequired["aws_sdk_iot.types.index_name.IndexName"]
    """<p>The dynamic thing group index name.</p>"""
    query_string: NotRequired["aws_sdk_iot.types.query_string.QueryString"]
    """<p>The dynamic thing group search query string.</p>"""
    query_version: NotRequired["aws_sdk_iot.types.query_version.QueryVersion"]
    """<p>The dynamic thing group query version.</p>"""
    status: NotRequired["aws_sdk_iot.types.dynamic_group_status.DynamicGroupStatus"]
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
        import aws_sdk_iot.types.thing_group_properties

        out["thingGroupProperties"] = (
            aws_sdk_iot.types.thing_group_properties.serialize_json(
                value["thing_group_properties"]
            )
        )
    if "thing_group_metadata" in value:
        import aws_sdk_iot.types.thing_group_metadata

        out["thingGroupMetadata"] = (
            aws_sdk_iot.types.thing_group_metadata.serialize_json(
                value["thing_group_metadata"]
            )
        )
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    if "status" in value:
        import aws_sdk_iot.types.dynamic_group_status

        out["status"] = aws_sdk_iot.types.dynamic_group_status.serialize_json(
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
        import aws_sdk_iot.types.thing_group_properties

        out["thing_group_properties"] = (
            aws_sdk_iot.types.thing_group_properties.deserialize_json(
                data["thingGroupProperties"]
            )
        )
    if "thingGroupMetadata" in data:
        import aws_sdk_iot.types.thing_group_metadata

        out["thing_group_metadata"] = (
            aws_sdk_iot.types.thing_group_metadata.deserialize_json(
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
        import aws_sdk_iot.types.dynamic_group_status

        out["status"] = aws_sdk_iot.types.dynamic_group_status.deserialize_json(
            data["status"]
        )
    return out
