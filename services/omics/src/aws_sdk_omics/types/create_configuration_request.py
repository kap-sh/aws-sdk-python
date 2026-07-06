"""Generated from Smithy shape ``com.amazonaws.omics#CreateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.configuration_description
    import aws_sdk_omics.types.configuration_name
    import aws_sdk_omics.types.configuration_request_id
    import aws_sdk_omics.types.run_configurations
    import aws_sdk_omics.types.tag_map


class CreateConfigurationRequest(TypedDict, closed=True):
    name: "aws_sdk_omics.types.configuration_name.ConfigurationName"
    """<p>User-friendly name for the configuration.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.configuration_description.ConfigurationDescription"
    ]
    """<p>Optional description for the configuration.</p>"""
    run_configurations: "aws_sdk_omics.types.run_configurations.RunConfigurations"
    """<p>Required run-specific configurations.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>Optional tags for the configuration.</p>"""
    request_id: "aws_sdk_omics.types.configuration_request_id.ConfigurationRequestId"
    """<p>Optional request idempotency token. If not specified, a universally unique identifier (UUID) will be automatically generated for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_omics.types.run_configurations

    out["runConfigurations"] = aws_sdk_omics.types.run_configurations.serialize_json(
        value["run_configurations"]
    )
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    out["requestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateConfigurationRequest:
    out: CreateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateConfigurationRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "runConfigurations" in data:
        import aws_sdk_omics.types.run_configurations

        out["run_configurations"] = (
            aws_sdk_omics.types.run_configurations.deserialize_json(
                data["runConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfigurationRequest.run_configurations required"
        )
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("CreateConfigurationRequest.request_id required")
    return out
