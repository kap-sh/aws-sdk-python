"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.monitor_list
    import aws_sdk_appconfig.types.name
    import aws_sdk_appconfig.types.tag_map


class CreateEnvironmentRequest(TypedDict):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    name: "aws_sdk_appconfig.types.name.Name"
    """<p>A name for the environment.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>A description of the environment.</p>"""
    monitors: NotRequired["aws_sdk_appconfig.types.monitor_list.MonitorList"]
    """<p>Amazon CloudWatch alarms to monitor during the deployment process.</p>"""
    tags: NotRequired["aws_sdk_appconfig.types.tag_map.TagMap"]
    """<p>Metadata to assign to the environment. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "monitors" in value:
        import aws_sdk_appconfig.types.monitor_list

        out["Monitors"] = aws_sdk_appconfig.types.monitor_list.serialize_json(
            value["monitors"]
        )
    if "tags" in value:
        import aws_sdk_appconfig.types.tag_map

        out["Tags"] = aws_sdk_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEnvironmentRequest:
    out: CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateEnvironmentRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Monitors" in data:
        import aws_sdk_appconfig.types.monitor_list

        out["monitors"] = aws_sdk_appconfig.types.monitor_list.deserialize_json(
            data["Monitors"]
        )
    if "Tags" in data:
        import aws_sdk_appconfig.types.tag_map

        out["tags"] = aws_sdk_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out
