"""Generated from Smithy shape ``com.amazonaws.connect#View``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp
    import aws_sdk_connect.types.view_content
    import aws_sdk_connect.types.view_content_sha256
    import aws_sdk_connect.types.view_description
    import aws_sdk_connect.types.view_id
    import aws_sdk_connect.types.view_name
    import aws_sdk_connect.types.view_status
    import aws_sdk_connect.types.view_type
    import aws_sdk_connect.types.view_version


class View(TypedDict):
    id: NotRequired["aws_sdk_connect.types.view_id.ViewId"]
    """<p>The identifier of the view.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view.</p>"""
    name: NotRequired["aws_sdk_connect.types.view_name.ViewName"]
    """<p>The name of the view.</p>"""
    status: NotRequired["aws_sdk_connect.types.view_status.ViewStatus"]
    """<p>Indicates the view status as either <code>SAVED</code> or <code>PUBLISHED</code>. The <code>PUBLISHED</code> status will initiate validation on the content.</p>"""
    type: NotRequired["aws_sdk_connect.types.view_type.ViewType"]
    """<p>The type of the view - <code>CUSTOMER_MANAGED</code>.</p>"""
    description: NotRequired["aws_sdk_connect.types.view_description.ViewDescription"]
    """<p>The description of the view.</p>"""
    version: "aws_sdk_connect.types.view_version.ViewVersion"
    """<p>Current version of the view.</p>"""
    version_description: NotRequired[
        "aws_sdk_connect.types.view_description.ViewDescription"
    ]
    """<p>The description of the version.</p>"""
    content: NotRequired["aws_sdk_connect.types.view_content.ViewContent"]
    """<p>View content containing all content necessary to render a view except for runtime input data.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags associated with the view resource (not specific to view version).</p>"""
    created_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp of when the view was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>Latest timestamp of the <code>UpdateViewContent</code> or <code>CreateViewVersion</code> operations.</p>"""
    view_content_sha256: NotRequired[
        "aws_sdk_connect.types.view_content_sha256.ViewContentSha256"
    ]
    """<p>Indicates the checksum value of the latest published view content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: View) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_connect.types.view_status

        out["Status"] = aws_sdk_connect.types.view_status.serialize_json(
            value["status"]
        )
    if "type" in value:
        import aws_sdk_connect.types.view_type

        out["Type"] = aws_sdk_connect.types.view_type.serialize_json(value["type"])
    if "description" in value:
        out["Description"] = value["description"]
    out["Version"] = value.get("version", 0)
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "content" in value:
        import aws_sdk_connect.types.view_content

        out["Content"] = aws_sdk_connect.types.view_content.serialize_json(
            value["content"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "created_time" in value:
        import aws_sdk_connect.types.timestamp

        out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "view_content_sha256" in value:
        out["ViewContentSha256"] = value["view_content_sha256"]
    return out


def deserialize_json(data: dict) -> View:
    out: View = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_connect.types.view_status

        out["status"] = aws_sdk_connect.types.view_status.deserialize_json(
            data["Status"]
        )
    if "Type" in data:
        import aws_sdk_connect.types.view_type

        out["type"] = aws_sdk_connect.types.view_type.deserialize_json(data["Type"])
    if "Description" in data:
        out["description"] = data["Description"]
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "Content" in data:
        import aws_sdk_connect.types.view_content

        out["content"] = aws_sdk_connect.types.view_content.deserialize_json(
            data["Content"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "ViewContentSha256" in data:
        out["view_content_sha256"] = data["ViewContentSha256"]
    return out
