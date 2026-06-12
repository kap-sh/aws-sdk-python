"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CreateCustomPluginRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string_max1024
    import aws_sdk_kafkaconnect.types.__string_min1_max128
    import aws_sdk_kafkaconnect.types.custom_plugin_content_type
    import aws_sdk_kafkaconnect.types.custom_plugin_location
    import aws_sdk_kafkaconnect.types.tags


class CreateCustomPluginRequest(TypedDict):
    content_type: (
        "aws_sdk_kafkaconnect.types.custom_plugin_content_type.CustomPluginContentType"
    )
    """<p>The type of the plugin file.</p>"""
    description: NotRequired[
        "aws_sdk_kafkaconnect.types.__string_max1024.__stringMax1024"
    ]
    """<p>A summary description of the custom plugin.</p>"""
    location: "aws_sdk_kafkaconnect.types.custom_plugin_location.CustomPluginLocation"
    """<p>Information about the location of a custom plugin.</p>"""
    name: "aws_sdk_kafkaconnect.types.__string_min1_max128.__stringMin1Max128"
    """<p>The name of the custom plugin.</p>"""
    tags: NotRequired["aws_sdk_kafkaconnect.types.tags.Tags"]
    """<p>The tags you want to attach to the custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomPluginRequest) -> dict:
    out: dict = {}
    out["contentType"] = value["content_type"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_kafkaconnect.types.custom_plugin_location

    out["location"] = aws_sdk_kafkaconnect.types.custom_plugin_location.serialize_json(
        value["location"]
    )
    out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_kafkaconnect.types.tags

        out["tags"] = aws_sdk_kafkaconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCustomPluginRequest:
    out: CreateCustomPluginRequest = {}  # type: ignore[typeddict-item]
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("CreateCustomPluginRequest.content_type required")
    if "description" in data:
        out["description"] = data["description"]
    if "location" in data:
        import aws_sdk_kafkaconnect.types.custom_plugin_location

        out["location"] = (
            aws_sdk_kafkaconnect.types.custom_plugin_location.deserialize_json(
                data["location"]
            )
        )
    else:
        raise DeserializationError("CreateCustomPluginRequest.location required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCustomPluginRequest.name required")
    if "tags" in data:
        import aws_sdk_kafkaconnect.types.tags

        out["tags"] = aws_sdk_kafkaconnect.types.tags.deserialize_json(data["tags"])
    return out
