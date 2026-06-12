"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CustomPluginRevisionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__long
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.__timestamp_iso8601
    import aws_sdk_kafkaconnect.types.custom_plugin_content_type
    import aws_sdk_kafkaconnect.types.custom_plugin_file_description
    import aws_sdk_kafkaconnect.types.custom_plugin_location_description


class CustomPluginRevisionSummary(TypedDict):
    content_type: NotRequired[
        "aws_sdk_kafkaconnect.types.custom_plugin_content_type.CustomPluginContentType"
    ]
    """<p>The format of the plugin file.</p>"""
    creation_time: NotRequired[
        "aws_sdk_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that the custom plugin was created.</p>"""
    description: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The description of the custom plugin.</p>"""
    file_description: NotRequired[
        "aws_sdk_kafkaconnect.types.custom_plugin_file_description.CustomPluginFileDescription"
    ]
    """<p>Details about the custom plugin file.</p>"""
    location: NotRequired[
        "aws_sdk_kafkaconnect.types.custom_plugin_location_description.CustomPluginLocationDescription"
    ]
    """<p>Information about the location of the custom plugin.</p>"""
    revision: "aws_sdk_kafkaconnect.types.__long.__long"
    """<p>The revision of the custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPluginRevisionSummary) -> dict:
    out: dict = {}
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "creation_time" in value:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "file_description" in value:
        import aws_sdk_kafkaconnect.types.custom_plugin_file_description

        out["fileDescription"] = (
            aws_sdk_kafkaconnect.types.custom_plugin_file_description.serialize_json(
                value["file_description"]
            )
        )
    if "location" in value:
        import aws_sdk_kafkaconnect.types.custom_plugin_location_description

        out["location"] = (
            aws_sdk_kafkaconnect.types.custom_plugin_location_description.serialize_json(
                value["location"]
            )
        )
    out["revision"] = value.get("revision", 0)
    return out


def deserialize_json(data: dict) -> CustomPluginRevisionSummary:
    out: CustomPluginRevisionSummary = {}  # type: ignore[typeddict-item]
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    if "creationTime" in data:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "fileDescription" in data:
        import aws_sdk_kafkaconnect.types.custom_plugin_file_description

        out["file_description"] = (
            aws_sdk_kafkaconnect.types.custom_plugin_file_description.deserialize_json(
                data["fileDescription"]
            )
        )
    if "location" in data:
        import aws_sdk_kafkaconnect.types.custom_plugin_location_description

        out["location"] = (
            aws_sdk_kafkaconnect.types.custom_plugin_location_description.deserialize_json(
                data["location"]
            )
        )
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    return out
