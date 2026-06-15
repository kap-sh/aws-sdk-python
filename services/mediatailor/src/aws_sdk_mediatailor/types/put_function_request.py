"""Generated from Smithy shape ``com.amazonaws.mediatailor#PutFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.custom_output_configuration
    import aws_sdk_mediatailor.types.function_type
    import aws_sdk_mediatailor.types.http_request_configuration
    import aws_sdk_mediatailor.types.sequential_executor_configuration


class PutFunctionRequest(TypedDict):
    function_id: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The identifier of the function. The identifier must be unique within your account.</p>"""
    function_type: "aws_sdk_mediatailor.types.function_type.FunctionType"
    r"""<p>The type of the function. The function type determines what the function can do at runtime. Valid values: <code>CUSTOM_OUTPUT</code> evaluates expressions and produces output bindings with no external calls. <code>HTTP_REQUEST</code> makes an HTTP call to an external service and evaluates output expressions that can reference the response. <code>SEQUENTIAL_EXECUTOR</code> runs a sequence of child functions in order, passing data between steps through temporary data. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types.html\">Function types and composition</a> in the <i>MediaTailor User Guide</i>.</p>"""
    description: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>A description of the function.</p>"""
    http_request_configuration: NotRequired[
        "aws_sdk_mediatailor.types.http_request_configuration.HttpRequestConfiguration"
    ]
    """<p>The configuration for an <code>HTTP_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>HTTP_REQUEST</code>.</p>"""
    custom_output_configuration: NotRequired[
        "aws_sdk_mediatailor.types.custom_output_configuration.CustomOutputConfiguration"
    ]
    """<p>The configuration for a <code>CUSTOM_OUTPUT</code> function. Specifies the runtime and output expressions. Required when <code>FunctionType</code> is <code>CUSTOM_OUTPUT</code>.</p>"""
    sequential_executor_configuration: NotRequired[
        "aws_sdk_mediatailor.types.sequential_executor_configuration.SequentialExecutorConfiguration"
    ]
    """<p>The configuration for a <code>SEQUENTIAL_EXECUTOR</code> function. Specifies the ordered list of child functions to execute, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>SEQUENTIAL_EXECUTOR</code>.</p>"""
    tags: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    r"""<p>The tags to assign to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionRequest) -> dict:
    out: dict = {}
    import aws_sdk_mediatailor.types.function_type

    out["FunctionType"] = aws_sdk_mediatailor.types.function_type.serialize_json(
        value["function_type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "http_request_configuration" in value:
        import aws_sdk_mediatailor.types.http_request_configuration

        out["HttpRequestConfiguration"] = (
            aws_sdk_mediatailor.types.http_request_configuration.serialize_json(
                value["http_request_configuration"]
            )
        )
    if "custom_output_configuration" in value:
        import aws_sdk_mediatailor.types.custom_output_configuration

        out["CustomOutputConfiguration"] = (
            aws_sdk_mediatailor.types.custom_output_configuration.serialize_json(
                value["custom_output_configuration"]
            )
        )
    if "sequential_executor_configuration" in value:
        import aws_sdk_mediatailor.types.sequential_executor_configuration

        out["SequentialExecutorConfiguration"] = (
            aws_sdk_mediatailor.types.sequential_executor_configuration.serialize_json(
                value["sequential_executor_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> PutFunctionRequest:
    out: PutFunctionRequest = {}  # type: ignore[typeddict-item]
    if "FunctionType" in data:
        import aws_sdk_mediatailor.types.function_type

        out["function_type"] = aws_sdk_mediatailor.types.function_type.deserialize_json(
            data["FunctionType"]
        )
    else:
        raise DeserializationError("PutFunctionRequest.function_type required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "HttpRequestConfiguration" in data:
        import aws_sdk_mediatailor.types.http_request_configuration

        out["http_request_configuration"] = (
            aws_sdk_mediatailor.types.http_request_configuration.deserialize_json(
                data["HttpRequestConfiguration"]
            )
        )
    if "CustomOutputConfiguration" in data:
        import aws_sdk_mediatailor.types.custom_output_configuration

        out["custom_output_configuration"] = (
            aws_sdk_mediatailor.types.custom_output_configuration.deserialize_json(
                data["CustomOutputConfiguration"]
            )
        )
    if "SequentialExecutorConfiguration" in data:
        import aws_sdk_mediatailor.types.sequential_executor_configuration

        out["sequential_executor_configuration"] = (
            aws_sdk_mediatailor.types.sequential_executor_configuration.deserialize_json(
                data["SequentialExecutorConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["tags"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
