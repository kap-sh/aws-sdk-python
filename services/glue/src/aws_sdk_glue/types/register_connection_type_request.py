"""Generated from Smithy shape ``com.amazonaws.glue#RegisterConnectionTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection_properties_configuration
    import aws_sdk_glue.types.connector_authentication_configuration
    import aws_sdk_glue.types.description
    import aws_sdk_glue.types.integration_type
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.rest_configuration
    import aws_sdk_glue.types.tags_map


class RegisterConnectionTypeRequest(TypedDict):
    connection_type: "aws_sdk_glue.types.name_string.NameString"
    r"""<p>The name of the connection type. Must be between 1 and 255 characters and must be prefixed with \"REST-\" to indicate it is a REST-based connector.</p>"""
    integration_type: "aws_sdk_glue.types.integration_type.IntegrationType"
    r"""<p>The integration type for the connection. Currently only \"REST\" protocol is supported.</p>"""
    description: NotRequired["aws_sdk_glue.types.description.Description"]
    """<p>A description of the connection type. Can be up to 2048 characters and provides details about the purpose and functionality of the connection type.</p>"""
    connection_properties: "aws_sdk_glue.types.connection_properties_configuration.ConnectionPropertiesConfiguration"
    """<p>Defines the base URL and additional request parameters needed during connection creation for this connection type.</p>"""
    connector_authentication_configuration: "aws_sdk_glue.types.connector_authentication_configuration.ConnectorAuthenticationConfiguration"
    """<p>Defines the supported authentication types and required properties for this connection type, including Basic, OAuth2, and Custom authentication methods.</p>"""
    rest_configuration: "aws_sdk_glue.types.rest_configuration.RestConfiguration"
    """<p>Defines the HTTP request and response configuration, validation endpoint, and entity configurations for REST API interactions.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>The tags you assign to the connection type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterConnectionTypeRequest) -> dict:
    out: dict = {}
    out["ConnectionType"] = value["connection_type"]
    import aws_sdk_glue.types.integration_type

    out["IntegrationType"] = aws_sdk_glue.types.integration_type.serialize_aws_json_1_1(
        value["integration_type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_glue.types.connection_properties_configuration

    out["ConnectionProperties"] = (
        aws_sdk_glue.types.connection_properties_configuration.serialize_aws_json_1_1(
            value["connection_properties"]
        )
    )
    import aws_sdk_glue.types.connector_authentication_configuration

    out["ConnectorAuthenticationConfiguration"] = (
        aws_sdk_glue.types.connector_authentication_configuration.serialize_aws_json_1_1(
            value["connector_authentication_configuration"]
        )
    )
    import aws_sdk_glue.types.rest_configuration

    out["RestConfiguration"] = (
        aws_sdk_glue.types.rest_configuration.serialize_aws_json_1_1(
            value["rest_configuration"]
        )
    )
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterConnectionTypeRequest:
    out: RegisterConnectionTypeRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.connection_type required"
        )
    if "IntegrationType" in data:
        import aws_sdk_glue.types.integration_type

        out["integration_type"] = (
            aws_sdk_glue.types.integration_type.deserialize_aws_json_1_1(
                data["IntegrationType"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.integration_type required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ConnectionProperties" in data:
        import aws_sdk_glue.types.connection_properties_configuration

        out["connection_properties"] = (
            aws_sdk_glue.types.connection_properties_configuration.deserialize_aws_json_1_1(
                data["ConnectionProperties"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.connection_properties required"
        )
    if "ConnectorAuthenticationConfiguration" in data:
        import aws_sdk_glue.types.connector_authentication_configuration

        out["connector_authentication_configuration"] = (
            aws_sdk_glue.types.connector_authentication_configuration.deserialize_aws_json_1_1(
                data["ConnectorAuthenticationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.connector_authentication_configuration required"
        )
    if "RestConfiguration" in data:
        import aws_sdk_glue.types.rest_configuration

        out["rest_configuration"] = (
            aws_sdk_glue.types.rest_configuration.deserialize_aws_json_1_1(
                data["RestConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterConnectionTypeRequest.rest_configuration required"
        )
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
