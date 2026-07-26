"""Generated from Smithy shape ``com.amazonaws.apigateway#RestApi``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.api_key_source_type
    import capo_api_gateway.types.api_status
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.endpoint_access_mode
    import capo_api_gateway.types.endpoint_configuration
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.security_policy
    import capo_api_gateway.types.string
    import capo_api_gateway.types.timestamp


class RestApi(TypedDict, closed=True):
    id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The API's identifier. This identifier is unique across all of your APIs in API Gateway.</p>"""
    name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The API's name.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The API's description.</p>"""
    created_date: NotRequired["capo_api_gateway.types.timestamp.Timestamp"]
    """<p>The timestamp when the API was created.</p>"""
    version: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A version identifier for the API.</p>"""
    warnings: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>The warning messages reported when <code>failonwarnings</code> is turned on during API import.</p>"""
    binary_media_types: NotRequired[
        "capo_api_gateway.types.list_of_string.ListOfString"
    ]
    """<p>The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</p>"""
    minimum_compression_size: NotRequired[
        "capo_api_gateway.types.nullable_integer.NullableInteger"
    ]
    """<p>A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.</p>"""
    api_key_source: NotRequired[
        "capo_api_gateway.types.api_key_source_type.ApiKeySourceType"
    ]
    """<p>The source of the API key for metering requests according to a usage plan. Valid values are: ><code>HEADER</code> to read the API key from the <code>X-API-Key</code> header of a request. <code>AUTHORIZER</code> to read the API key from the <code>UsageIdentifierKey</code> from a custom authorizer.</p>"""
    endpoint_configuration: NotRequired[
        "capo_api_gateway.types.endpoint_configuration.EndpointConfiguration"
    ]
    """<p>The endpoint configuration of this RestApi showing the endpoint types and IP address types of the API. </p>"""
    policy: NotRequired["capo_api_gateway.types.string.String"]
    """<p>A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.</p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The collection of tags. Each tag element is associated with a given resource.</p>"""
    disable_execute_api_endpoint: "capo_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether clients can invoke your API by using the default <code>execute-api</code> endpoint. By default, clients can invoke your API with the default <code>https://{api_id}.execute-api.{region}.amazonaws.com</code> endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.</p>"""
    root_resource_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The API's root resource ID.</p>"""
    security_policy: NotRequired[
        "capo_api_gateway.types.security_policy.SecurityPolicy"
    ]
    """<p> The Transport Layer Security (TLS) version + cipher suite for this RestApi. </p>"""
    endpoint_access_mode: NotRequired[
        "capo_api_gateway.types.endpoint_access_mode.EndpointAccessMode"
    ]
    """<p> The endpoint access mode of the RestApi. </p>"""
    api_status: NotRequired["capo_api_gateway.types.api_status.ApiStatus"]
    """<p>The ApiStatus of the RestApi. </p>"""
    api_status_message: NotRequired["capo_api_gateway.types.string.String"]
    """<p> The status message of the RestApi. When the status message is <code>UPDATING</code> you can still invoke it. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestApi) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_date" in value:
        import capo_api_gateway.types.timestamp

        out["createdDate"] = capo_api_gateway.types.timestamp.serialize_json(
            value["created_date"]
        )
    if "version" in value:
        out["version"] = value["version"]
    if "warnings" in value:
        import capo_api_gateway.types.list_of_string

        out["warnings"] = capo_api_gateway.types.list_of_string.serialize_json(
            value["warnings"]
        )
    if "binary_media_types" in value:
        import capo_api_gateway.types.list_of_string

        out["binaryMediaTypes"] = capo_api_gateway.types.list_of_string.serialize_json(
            value["binary_media_types"]
        )
    if "minimum_compression_size" in value:
        out["minimumCompressionSize"] = value["minimum_compression_size"]
    if "api_key_source" in value:
        import capo_api_gateway.types.api_key_source_type

        out["apiKeySource"] = capo_api_gateway.types.api_key_source_type.serialize_json(
            value["api_key_source"]
        )
    if "endpoint_configuration" in value:
        import capo_api_gateway.types.endpoint_configuration

        out["endpointConfiguration"] = (
            capo_api_gateway.types.endpoint_configuration.serialize_json(
                value["endpoint_configuration"]
            )
        )
    if "policy" in value:
        out["policy"] = value["policy"]
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    out["disableExecuteApiEndpoint"] = value.get("disable_execute_api_endpoint", False)
    if "root_resource_id" in value:
        out["rootResourceId"] = value["root_resource_id"]
    if "security_policy" in value:
        import capo_api_gateway.types.security_policy

        out["securityPolicy"] = capo_api_gateway.types.security_policy.serialize_json(
            value["security_policy"]
        )
    if "endpoint_access_mode" in value:
        import capo_api_gateway.types.endpoint_access_mode

        out["endpointAccessMode"] = (
            capo_api_gateway.types.endpoint_access_mode.serialize_json(
                value["endpoint_access_mode"]
            )
        )
    if "api_status" in value:
        import capo_api_gateway.types.api_status

        out["apiStatus"] = capo_api_gateway.types.api_status.serialize_json(
            value["api_status"]
        )
    if "api_status_message" in value:
        out["apiStatusMessage"] = value["api_status_message"]
    return out


def deserialize_json(data: dict) -> RestApi:
    out: RestApi = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdDate" in data:
        import capo_api_gateway.types.timestamp

        out["created_date"] = capo_api_gateway.types.timestamp.deserialize_json(
            data["createdDate"]
        )
    if "version" in data:
        out["version"] = data["version"]
    if "warnings" in data:
        import capo_api_gateway.types.list_of_string

        out["warnings"] = capo_api_gateway.types.list_of_string.deserialize_json(
            data["warnings"]
        )
    if "binaryMediaTypes" in data:
        import capo_api_gateway.types.list_of_string

        out["binary_media_types"] = (
            capo_api_gateway.types.list_of_string.deserialize_json(
                data["binaryMediaTypes"]
            )
        )
    if "minimumCompressionSize" in data:
        out["minimum_compression_size"] = data["minimumCompressionSize"]
    if "apiKeySource" in data:
        import capo_api_gateway.types.api_key_source_type

        out["api_key_source"] = (
            capo_api_gateway.types.api_key_source_type.deserialize_json(
                data["apiKeySource"]
            )
        )
    if "endpointConfiguration" in data:
        import capo_api_gateway.types.endpoint_configuration

        out["endpoint_configuration"] = (
            capo_api_gateway.types.endpoint_configuration.deserialize_json(
                data["endpointConfiguration"]
            )
        )
    if "policy" in data:
        out["policy"] = data["policy"]
    if "tags" in data:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    if "disableExecuteApiEndpoint" in data:
        out["disable_execute_api_endpoint"] = data["disableExecuteApiEndpoint"]
    else:
        out["disable_execute_api_endpoint"] = False
    if "rootResourceId" in data:
        out["root_resource_id"] = data["rootResourceId"]
    if "securityPolicy" in data:
        import capo_api_gateway.types.security_policy

        out["security_policy"] = (
            capo_api_gateway.types.security_policy.deserialize_json(
                data["securityPolicy"]
            )
        )
    if "endpointAccessMode" in data:
        import capo_api_gateway.types.endpoint_access_mode

        out["endpoint_access_mode"] = (
            capo_api_gateway.types.endpoint_access_mode.deserialize_json(
                data["endpointAccessMode"]
            )
        )
    if "apiStatus" in data:
        import capo_api_gateway.types.api_status

        out["api_status"] = capo_api_gateway.types.api_status.deserialize_json(
            data["apiStatus"]
        )
    if "apiStatusMessage" in data:
        out["api_status_message"] = data["apiStatusMessage"]
    return out
