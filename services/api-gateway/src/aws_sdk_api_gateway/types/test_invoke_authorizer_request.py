"""Generated from Smithy shape ``com.amazonaws.apigateway#TestInvokeAuthorizerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.map_of_string_to_list
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string


class TestInvokeAuthorizerRequest(TypedDict):
    rest_api_id: "aws_sdk_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    authorizer_id: "aws_sdk_api_gateway.types.string.String"
    """<p>Specifies a test invoke authorizer request's Authorizer ID.</p>"""
    headers: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A key-value map of headers to simulate an incoming invocation request. This is where the incoming authorization token, or identity source, should be specified.</p>"""
    multi_value_headers: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_list.MapOfStringToList"
    ]
    """<p>The headers as a map from string to list of values to simulate an incoming invocation request. This is where the incoming authorization token, or identity source, may be specified.</p>"""
    path_with_query_string: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.</p>"""
    body: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The simulated request body of an incoming invocation request.</p>"""
    stage_variables: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A key-value map of stage variables to simulate an invocation on a deployed Stage.</p>"""
    additional_context: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A key-value map of additional context variables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestInvokeAuthorizerRequest) -> dict:
    out: dict = {}
    if "headers" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["headers"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
                value["headers"]
            )
        )
    if "multi_value_headers" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_list

        out["multiValueHeaders"] = (
            aws_sdk_api_gateway.types.map_of_string_to_list.serialize_json(
                value["multi_value_headers"]
            )
        )
    if "path_with_query_string" in value:
        out["pathWithQueryString"] = value["path_with_query_string"]
    if "body" in value:
        out["body"] = value["body"]
    if "stage_variables" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["stageVariables"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
                value["stage_variables"]
            )
        )
    if "additional_context" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["additionalContext"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
                value["additional_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestInvokeAuthorizerRequest:
    out: TestInvokeAuthorizerRequest = {}  # type: ignore[typeddict-item]
    if "headers" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["headers"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["headers"]
            )
        )
    if "multiValueHeaders" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_list

        out["multi_value_headers"] = (
            aws_sdk_api_gateway.types.map_of_string_to_list.deserialize_json(
                data["multiValueHeaders"]
            )
        )
    if "pathWithQueryString" in data:
        out["path_with_query_string"] = data["pathWithQueryString"]
    if "body" in data:
        out["body"] = data["body"]
    if "stageVariables" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["stage_variables"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["stageVariables"]
            )
        )
    if "additionalContext" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["additional_context"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["additionalContext"]
            )
        )
    return out
