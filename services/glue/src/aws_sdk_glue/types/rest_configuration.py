"""Generated from Smithy shape ``com.amazonaws.glue#RestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.entity_configuration_map
    import aws_sdk_glue.types.source_configuration


class RestConfiguration(TypedDict, closed=True):
    global_source_configuration: NotRequired[
        "aws_sdk_glue.types.source_configuration.SourceConfiguration"
    ]
    """<p>Global configuration settings that apply to all REST API requests for this connection type, including common request methods, paths, and parameters.</p>"""
    validation_endpoint_configuration: NotRequired[
        "aws_sdk_glue.types.source_configuration.SourceConfiguration"
    ]
    """<p>Configuration for the endpoint used to validate connection credentials and test connectivity during connection creation.</p>"""
    entity_configurations: NotRequired[
        "aws_sdk_glue.types.entity_configuration_map.EntityConfigurationMap"
    ]
    """<p>A map of entity configurations that define how to interact with different data entities available through the REST API, including their schemas and access patterns.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestConfiguration) -> dict:
    out: dict = {}
    if "global_source_configuration" in value:
        import aws_sdk_glue.types.source_configuration

        out["GlobalSourceConfiguration"] = (
            aws_sdk_glue.types.source_configuration.serialize_aws_json_1_1(
                value["global_source_configuration"]
            )
        )
    if "validation_endpoint_configuration" in value:
        import aws_sdk_glue.types.source_configuration

        out["ValidationEndpointConfiguration"] = (
            aws_sdk_glue.types.source_configuration.serialize_aws_json_1_1(
                value["validation_endpoint_configuration"]
            )
        )
    if "entity_configurations" in value:
        import aws_sdk_glue.types.entity_configuration_map

        out["EntityConfigurations"] = (
            aws_sdk_glue.types.entity_configuration_map.serialize_aws_json_1_1(
                value["entity_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestConfiguration:
    out: RestConfiguration = {}  # type: ignore[typeddict-item]
    if "GlobalSourceConfiguration" in data:
        import aws_sdk_glue.types.source_configuration

        out["global_source_configuration"] = (
            aws_sdk_glue.types.source_configuration.deserialize_aws_json_1_1(
                data["GlobalSourceConfiguration"]
            )
        )
    if "ValidationEndpointConfiguration" in data:
        import aws_sdk_glue.types.source_configuration

        out["validation_endpoint_configuration"] = (
            aws_sdk_glue.types.source_configuration.deserialize_aws_json_1_1(
                data["ValidationEndpointConfiguration"]
            )
        )
    if "EntityConfigurations" in data:
        import aws_sdk_glue.types.entity_configuration_map

        out["entity_configurations"] = (
            aws_sdk_glue.types.entity_configuration_map.deserialize_aws_json_1_1(
                data["EntityConfigurations"]
            )
        )
    return out
