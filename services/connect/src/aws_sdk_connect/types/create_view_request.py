"""Generated from Smithy shape ``com.amazonaws.connect#CreateViewRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.view_description
    import aws_sdk_connect.types.view_input_content
    import aws_sdk_connect.types.view_name
    import aws_sdk_connect.types.view_status
    import aws_sdk_connect.types.views_client_token
    import aws_sdk_connect.types.views_instance_id


class CreateViewRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.views_instance_id.ViewsInstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    client_token: NotRequired[
        "aws_sdk_connect.types.views_client_token.ViewsClientToken"
    ]
    """<p>A unique Id for each create view request to avoid duplicate view creation. For example, the view is idempotent ClientToken is provided.</p>"""
    status: "aws_sdk_connect.types.view_status.ViewStatus"
    """<p>Indicates the view status as either <code>SAVED</code> or <code>PUBLISHED</code>. The <code>PUBLISHED</code> status will initiate validation on the content.</p>"""
    content: "aws_sdk_connect.types.view_input_content.ViewInputContent"
    """<p>View content containing all content necessary to render a view except for runtime input data.</p> <p>The total uncompressed content has a maximum file size of 400kB.</p>"""
    description: NotRequired["aws_sdk_connect.types.view_description.ViewDescription"]
    """<p>The description of the view.</p>"""
    name: "aws_sdk_connect.types.view_name.ViewName"
    """<p>The name of the view.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags associated with the view resource (not specific to view version).These tags can be used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateViewRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import aws_sdk_connect.types.view_status

    out["Status"] = aws_sdk_connect.types.view_status.serialize_json(value["status"])
    import aws_sdk_connect.types.view_input_content

    out["Content"] = aws_sdk_connect.types.view_input_content.serialize_json(
        value["content"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateViewRequest:
    out: CreateViewRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Status" in data:
        import aws_sdk_connect.types.view_status

        out["status"] = aws_sdk_connect.types.view_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("CreateViewRequest.status required")
    if "Content" in data:
        import aws_sdk_connect.types.view_input_content

        out["content"] = aws_sdk_connect.types.view_input_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("CreateViewRequest.content required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateViewRequest.name required")
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
