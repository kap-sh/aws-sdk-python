"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.actions_map
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.extension_or_parameter_name
    import aws_sdk_appconfig.types.integer
    import aws_sdk_appconfig.types.parameter_map
    import aws_sdk_appconfig.types.tag_map


class CreateExtensionRequest(TypedDict, closed=True):
    name: "aws_sdk_appconfig.types.extension_or_parameter_name.ExtensionOrParameterName"
    """<p>A name for the extension. Each extension name in your account must be unique. Extension versions use the same name.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>Information about the extension.</p>"""
    actions: "aws_sdk_appconfig.types.actions_map.ActionsMap"
    """<p>The actions defined in the extension.</p>"""
    parameters: NotRequired["aws_sdk_appconfig.types.parameter_map.ParameterMap"]
    """<p>The parameters accepted by the extension. You specify parameter values when you associate the extension to an AppConfig resource by using the <code>CreateExtensionAssociation</code> API action. For Lambda extension actions, these parameters are included in the Lambda request object.</p>"""
    tags: NotRequired["aws_sdk_appconfig.types.tag_map.TagMap"]
    """<p>Adds one or more tags for the specified extension. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. </p>"""
    latest_version_number: NotRequired["aws_sdk_appconfig.types.integer.Integer"]
    """<p>You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExtensionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_appconfig.types.actions_map

    out["Actions"] = aws_sdk_appconfig.types.actions_map.serialize_json(
        value["actions"]
    )
    if "parameters" in value:
        import aws_sdk_appconfig.types.parameter_map

        out["Parameters"] = aws_sdk_appconfig.types.parameter_map.serialize_json(
            value["parameters"]
        )
    if "tags" in value:
        import aws_sdk_appconfig.types.tag_map

        out["Tags"] = aws_sdk_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateExtensionRequest:
    out: CreateExtensionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateExtensionRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Actions" in data:
        import aws_sdk_appconfig.types.actions_map

        out["actions"] = aws_sdk_appconfig.types.actions_map.deserialize_json(
            data["Actions"]
        )
    else:
        raise DeserializationError("CreateExtensionRequest.actions required")
    if "Parameters" in data:
        import aws_sdk_appconfig.types.parameter_map

        out["parameters"] = aws_sdk_appconfig.types.parameter_map.deserialize_json(
            data["Parameters"]
        )
    if "Tags" in data:
        import aws_sdk_appconfig.types.tag_map

        out["tags"] = aws_sdk_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out
