"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDynamicThingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.index_name
    import aws_sdk_iot.types.optional_version
    import aws_sdk_iot.types.query_string
    import aws_sdk_iot.types.query_version
    import aws_sdk_iot.types.thing_group_name
    import aws_sdk_iot.types.thing_group_properties


class UpdateDynamicThingGroupRequest(TypedDict, closed=True):
    thing_group_name: "aws_sdk_iot.types.thing_group_name.ThingGroupName"
    """<p>The name of the dynamic thing group to update.</p>"""
    thing_group_properties: (
        "aws_sdk_iot.types.thing_group_properties.ThingGroupProperties"
    )
    """<p>The dynamic thing group properties to update.</p>"""
    expected_version: NotRequired["aws_sdk_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the dynamic thing group to update.</p>"""
    index_name: NotRequired["aws_sdk_iot.types.index_name.IndexName"]
    """<p>The dynamic thing group index to update.</p> <note> <p>Currently one index is supported: <code>AWS_Things</code>.</p> </note>"""
    query_string: NotRequired["aws_sdk_iot.types.query_string.QueryString"]
    """<p>The dynamic thing group search query string to update.</p>"""
    query_version: NotRequired["aws_sdk_iot.types.query_version.QueryVersion"]
    r"""<p>The dynamic thing group query version to update.</p> <note> <p>Currently one query version is supported: \"2017-09-30\". If not specified, the query version defaults to this value.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDynamicThingGroupRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.thing_group_properties

    out["thingGroupProperties"] = (
        aws_sdk_iot.types.thing_group_properties.serialize_json(
            value["thing_group_properties"]
        )
    )
    if "expected_version" in value:
        out["expectedVersion"] = value["expected_version"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    return out


def deserialize_json(data: dict) -> UpdateDynamicThingGroupRequest:
    out: UpdateDynamicThingGroupRequest = {}  # type: ignore[typeddict-item]
    if "thingGroupProperties" in data:
        import aws_sdk_iot.types.thing_group_properties

        out["thing_group_properties"] = (
            aws_sdk_iot.types.thing_group_properties.deserialize_json(
                data["thingGroupProperties"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDynamicThingGroupRequest.thing_group_properties required"
        )
    if "expectedVersion" in data:
        out["expected_version"] = data["expectedVersion"]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "queryVersion" in data:
        out["query_version"] = data["queryVersion"]
    return out
