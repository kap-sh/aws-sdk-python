"""Generated from Smithy shape ``com.amazonaws.iot#CreateDynamicThingGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.index_name
    import aws_sdk_iot.types.query_string
    import aws_sdk_iot.types.query_version
    import aws_sdk_iot.types.tag_list
    import aws_sdk_iot.types.thing_group_name
    import aws_sdk_iot.types.thing_group_properties


class CreateDynamicThingGroupRequest(TypedDict):
    thing_group_name: "aws_sdk_iot.types.thing_group_name.ThingGroupName"
    """<p>The dynamic thing group name to create.</p>"""
    thing_group_properties: NotRequired[
        "aws_sdk_iot.types.thing_group_properties.ThingGroupProperties"
    ]
    """<p>The dynamic thing group properties.</p>"""
    index_name: NotRequired["aws_sdk_iot.types.index_name.IndexName"]
    """<p>The dynamic thing group index name.</p> <note> <p>Currently one index is supported: <code>AWS_Things</code>.</p> </note>"""
    query_string: "aws_sdk_iot.types.query_string.QueryString"
    r"""<p>The dynamic thing group search query string.</p> <p>See <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/query-syntax.html\">Query Syntax</a> for information about query string syntax.</p>"""
    query_version: NotRequired["aws_sdk_iot.types.query_version.QueryVersion"]
    r"""<p>The dynamic thing group query version.</p> <note> <p>Currently one query version is supported: \"2017-09-30\". If not specified, the query version defaults to this value.</p> </note>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the dynamic thing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDynamicThingGroupRequest) -> dict:
    out: dict = {}
    if "thing_group_properties" in value:
        import aws_sdk_iot.types.thing_group_properties

        out["thingGroupProperties"] = (
            aws_sdk_iot.types.thing_group_properties.serialize_json(
                value["thing_group_properties"]
            )
        )
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    out["queryString"] = value["query_string"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDynamicThingGroupRequest:
    out: CreateDynamicThingGroupRequest = {}  # type: ignore[typeddict-item]
    if "thingGroupProperties" in data:
        import aws_sdk_iot.types.thing_group_properties

        out["thing_group_properties"] = (
            aws_sdk_iot.types.thing_group_properties.deserialize_json(
                data["thingGroupProperties"]
            )
        )
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError(
            "CreateDynamicThingGroupRequest.query_string required"
        )
    if "queryVersion" in data:
        out["query_version"] = data["queryVersion"]
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
    return out
