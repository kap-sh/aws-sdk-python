"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CreateWorkerConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__sensitive_string
    import aws_sdk_kafkaconnect.types.__string_max1024
    import aws_sdk_kafkaconnect.types.__string_min1_max128
    import aws_sdk_kafkaconnect.types.tags


class CreateWorkerConfigurationRequest(TypedDict):
    description: NotRequired[
        "aws_sdk_kafkaconnect.types.__string_max1024.__stringMax1024"
    ]
    """<p>A summary description of the worker configuration.</p>"""
    name: "aws_sdk_kafkaconnect.types.__string_min1_max128.__stringMin1Max128"
    """<p>The name of the worker configuration.</p>"""
    properties_file_content: (
        "aws_sdk_kafkaconnect.types.__sensitive_string.__sensitiveString"
    )
    """<p>Base64 encoded contents of connect-distributed.properties file.</p>"""
    tags: NotRequired["aws_sdk_kafkaconnect.types.tags.Tags"]
    """<p>The tags you want to attach to the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkerConfigurationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    out["propertiesFileContent"] = value["properties_file_content"]
    if "tags" in value:
        import aws_sdk_kafkaconnect.types.tags

        out["tags"] = aws_sdk_kafkaconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWorkerConfigurationRequest:
    out: CreateWorkerConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkerConfigurationRequest.name required")
    if "propertiesFileContent" in data:
        out["properties_file_content"] = data["propertiesFileContent"]
    else:
        raise DeserializationError(
            "CreateWorkerConfigurationRequest.properties_file_content required"
        )
    if "tags" in data:
        import aws_sdk_kafkaconnect.types.tags

        out["tags"] = aws_sdk_kafkaconnect.types.tags.deserialize_json(data["tags"])
    return out
