"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateRestApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.api_key_source_type
    import aws_sdk_api_gateway.types.boolean
    import aws_sdk_api_gateway.types.endpoint_access_mode
    import aws_sdk_api_gateway.types.endpoint_configuration
    import aws_sdk_api_gateway.types.list_of_string
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.nullable_integer
    import aws_sdk_api_gateway.types.security_policy
    import aws_sdk_api_gateway.types.string


class CreateRestApiRequest(TypedDict, closed=True):
    name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the RestApi.</p>"""
    description: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The description of the RestApi.</p>"""
    version: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>A version identifier for the API.</p>"""
    clone_from: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The ID of the RestApi that you want to clone from.</p>"""
    binary_media_types: NotRequired[
        "aws_sdk_api_gateway.types.list_of_string.ListOfString"
    ]
    """<p>The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</p>"""
    minimum_compression_size: NotRequired[
        "aws_sdk_api_gateway.types.nullable_integer.NullableInteger"
    ]
    """<p>A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.</p>"""
    api_key_source: NotRequired[
        "aws_sdk_api_gateway.types.api_key_source_type.ApiKeySourceType"
    ]
    """<p>The source of the API key for metering requests according to a usage plan. Valid values are: <code>HEADER</code> to read the API key from the <code>X-API-Key</code> header of a request. <code>AUTHORIZER</code> to read the API key from the <code>UsageIdentifierKey</code> from a custom authorizer.</p>"""
    endpoint_configuration: NotRequired[
        "aws_sdk_api_gateway.types.endpoint_configuration.EndpointConfiguration"
    ]
    """<p>The endpoint configuration of this RestApi showing the endpoint types and IP address types of the API. </p>"""
    policy: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.</p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""
    disable_execute_api_endpoint: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether clients can invoke your API by using the default <code>execute-api</code> endpoint. By default, clients can invoke your API with the default <code>https://{api_id}.execute-api.{region}.amazonaws.com</code> endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint</p>"""
    security_policy: NotRequired[
        "aws_sdk_api_gateway.types.security_policy.SecurityPolicy"
    ]
    """<p> The Transport Layer Security (TLS) version + cipher suite for this RestApi. </p>"""
    endpoint_access_mode: NotRequired[
        "aws_sdk_api_gateway.types.endpoint_access_mode.EndpointAccessMode"
    ]
    """<p> The endpoint access mode of the RestApi. Only available for RestApis that use security policies that start with <code>SecurityPolicy_</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRestApiRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "version" in value:
        out["version"] = value["version"]
    if "clone_from" in value:
        out["cloneFrom"] = value["clone_from"]
    if "binary_media_types" in value:
        import aws_sdk_api_gateway.types.list_of_string

        out["binaryMediaTypes"] = (
            aws_sdk_api_gateway.types.list_of_string.serialize_json(
                value["binary_media_types"]
            )
        )
    if "minimum_compression_size" in value:
        out["minimumCompressionSize"] = value["minimum_compression_size"]
    if "api_key_source" in value:
        import aws_sdk_api_gateway.types.api_key_source_type

        out["apiKeySource"] = (
            aws_sdk_api_gateway.types.api_key_source_type.serialize_json(
                value["api_key_source"]
            )
        )
    if "endpoint_configuration" in value:
        import aws_sdk_api_gateway.types.endpoint_configuration

        out["endpointConfiguration"] = (
            aws_sdk_api_gateway.types.endpoint_configuration.serialize_json(
                value["endpoint_configuration"]
            )
        )
    if "policy" in value:
        out["policy"] = value["policy"]
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    out["disableExecuteApiEndpoint"] = value.get("disable_execute_api_endpoint", False)
    if "security_policy" in value:
        import aws_sdk_api_gateway.types.security_policy

        out["securityPolicy"] = (
            aws_sdk_api_gateway.types.security_policy.serialize_json(
                value["security_policy"]
            )
        )
    if "endpoint_access_mode" in value:
        import aws_sdk_api_gateway.types.endpoint_access_mode

        out["endpointAccessMode"] = (
            aws_sdk_api_gateway.types.endpoint_access_mode.serialize_json(
                value["endpoint_access_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRestApiRequest:
    out: CreateRestApiRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRestApiRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "version" in data:
        out["version"] = data["version"]
    if "cloneFrom" in data:
        out["clone_from"] = data["cloneFrom"]
    if "binaryMediaTypes" in data:
        import aws_sdk_api_gateway.types.list_of_string

        out["binary_media_types"] = (
            aws_sdk_api_gateway.types.list_of_string.deserialize_json(
                data["binaryMediaTypes"]
            )
        )
    if "minimumCompressionSize" in data:
        out["minimum_compression_size"] = data["minimumCompressionSize"]
    if "apiKeySource" in data:
        import aws_sdk_api_gateway.types.api_key_source_type

        out["api_key_source"] = (
            aws_sdk_api_gateway.types.api_key_source_type.deserialize_json(
                data["apiKeySource"]
            )
        )
    if "endpointConfiguration" in data:
        import aws_sdk_api_gateway.types.endpoint_configuration

        out["endpoint_configuration"] = (
            aws_sdk_api_gateway.types.endpoint_configuration.deserialize_json(
                data["endpointConfiguration"]
            )
        )
    if "policy" in data:
        out["policy"] = data["policy"]
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    if "disableExecuteApiEndpoint" in data:
        out["disable_execute_api_endpoint"] = data["disableExecuteApiEndpoint"]
    else:
        out["disable_execute_api_endpoint"] = False
    if "securityPolicy" in data:
        import aws_sdk_api_gateway.types.security_policy

        out["security_policy"] = (
            aws_sdk_api_gateway.types.security_policy.deserialize_json(
                data["securityPolicy"]
            )
        )
    if "endpointAccessMode" in data:
        import aws_sdk_api_gateway.types.endpoint_access_mode

        out["endpoint_access_mode"] = (
            aws_sdk_api_gateway.types.endpoint_access_mode.deserialize_json(
                data["endpointAccessMode"]
            )
        )
    return out
