"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_flow_content
    import aws_sdk_connect.types.contact_flow_description
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.contact_flow_name
    import aws_sdk_connect.types.contact_flow_state
    import aws_sdk_connect.types.contact_flow_status
    import aws_sdk_connect.types.contact_flow_type
    import aws_sdk_connect.types.flow_content_sha256
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.resource_version
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class ContactFlow(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    id: NotRequired["aws_sdk_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow.</p>"""
    name: NotRequired["aws_sdk_connect.types.contact_flow_name.ContactFlowName"]
    """<p>The name of the flow.</p>"""
    type: NotRequired["aws_sdk_connect.types.contact_flow_type.ContactFlowType"]
    r"""<p>The type of the flow. For descriptions of the available types, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types\">Choose a flow type</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    state: NotRequired["aws_sdk_connect.types.contact_flow_state.ContactFlowState"]
    """<p>The type of flow.</p>"""
    status: NotRequired["aws_sdk_connect.types.contact_flow_status.ContactFlowStatus"]
    """<p>The status of the flow.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the flow.</p>"""
    content: NotRequired[
        "aws_sdk_connect.types.contact_flow_content.ContactFlowContent"
    ]
    r"""<p>The JSON string that represents the content of the flow. For an example, see <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html\">Example flow in Connect Customer Flow language</a>. </p> <p>Length Constraints: Minimum length of 1. Maximum length of 256000.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    flow_content_sha256: NotRequired[
        "aws_sdk_connect.types.flow_content_sha256.FlowContentSha256"
    ]
    """<p>Indicates the checksum value of the flow content.</p>"""
    version: NotRequired["aws_sdk_connect.types.resource_version.ResourceVersion"]
    """<p>The identifier of the flow version.</p>"""
    version_description: NotRequired[
        "aws_sdk_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the flow version.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The time at which the flow was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The region in which the flow was last modified</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlow) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_connect.types.contact_flow_type

        out["Type"] = aws_sdk_connect.types.contact_flow_type.serialize_json(
            value["type"]
        )
    if "state" in value:
        import aws_sdk_connect.types.contact_flow_state

        out["State"] = aws_sdk_connect.types.contact_flow_state.serialize_json(
            value["state"]
        )
    if "status" in value:
        import aws_sdk_connect.types.contact_flow_status

        out["Status"] = aws_sdk_connect.types.contact_flow_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "content" in value:
        out["Content"] = value["content"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "flow_content_sha256" in value:
        out["FlowContentSha256"] = value["flow_content_sha256"]
    if "version" in value:
        out["Version"] = value["version"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ContactFlow:
    out: ContactFlow = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_connect.types.contact_flow_type

        out["type"] = aws_sdk_connect.types.contact_flow_type.deserialize_json(
            data["Type"]
        )
    if "State" in data:
        import aws_sdk_connect.types.contact_flow_state

        out["state"] = aws_sdk_connect.types.contact_flow_state.deserialize_json(
            data["State"]
        )
    if "Status" in data:
        import aws_sdk_connect.types.contact_flow_status

        out["status"] = aws_sdk_connect.types.contact_flow_status.deserialize_json(
            data["Status"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "FlowContentSha256" in data:
        out["flow_content_sha256"] = data["FlowContentSha256"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
