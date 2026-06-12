"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerConfigurationRevisionDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__long
    import aws_sdk_kafkaconnect.types.__sensitive_string
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.__timestamp_iso8601


class WorkerConfigurationRevisionDescription(TypedDict):
    creation_time: NotRequired[
        "aws_sdk_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that the worker configuration was created.</p>"""
    description: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The description of the worker configuration revision.</p>"""
    properties_file_content: NotRequired[
        "aws_sdk_kafkaconnect.types.__sensitive_string.__sensitiveString"
    ]
    """<p>Base64 encoded contents of the connect-distributed.properties file.</p>"""
    revision: "aws_sdk_kafkaconnect.types.__long.__long"
    """<p>The description of a revision of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerConfigurationRevisionDescription) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "properties_file_content" in value:
        out["propertiesFileContent"] = value["properties_file_content"]
    out["revision"] = value.get("revision", 0)
    return out


def deserialize_json(data: dict) -> WorkerConfigurationRevisionDescription:
    out: WorkerConfigurationRevisionDescription = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "propertiesFileContent" in data:
        out["properties_file_content"] = data["propertiesFileContent"]
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    return out
