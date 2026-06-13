"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#StartAsyncInvokeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.async_invoke_idempotency_token
    import aws_sdk_bedrock_runtime.types.async_invoke_identifier
    import aws_sdk_bedrock_runtime.types.async_invoke_output_data_config
    import aws_sdk_bedrock_runtime.types.model_input_payload
    import aws_sdk_bedrock_runtime.types.tag_list


class StartAsyncInvokeRequest(TypedDict):
    client_request_token: NotRequired[
        "aws_sdk_bedrock_runtime.types.async_invoke_idempotency_token.AsyncInvokeIdempotencyToken"
    ]
    """<p>Specify idempotency token to ensure that requests are not duplicated.</p>"""
    model_id: (
        "aws_sdk_bedrock_runtime.types.async_invoke_identifier.AsyncInvokeIdentifier"
    )
    """<p>The model to invoke.</p>"""
    model_input: "aws_sdk_bedrock_runtime.types.model_input_payload.ModelInputPayload"
    """<p>Input to send to the model.</p>"""
    output_data_config: "aws_sdk_bedrock_runtime.types.async_invoke_output_data_config.AsyncInvokeOutputDataConfig"
    """<p>Where to store the output.</p>"""
    tags: NotRequired["aws_sdk_bedrock_runtime.types.tag_list.TagList"]
    """<p>Tags to apply to the invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAsyncInvokeRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["modelId"] = value["model_id"]
    out["modelInput"] = value["model_input"]
    import aws_sdk_bedrock_runtime.types.async_invoke_output_data_config

    out["outputDataConfig"] = (
        aws_sdk_bedrock_runtime.types.async_invoke_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    if "tags" in value:
        import aws_sdk_bedrock_runtime.types.tag_list

        out["tags"] = aws_sdk_bedrock_runtime.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> StartAsyncInvokeRequest:
    out: StartAsyncInvokeRequest = {}  # type: ignore[typeddict-item]
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("StartAsyncInvokeRequest.model_id required")
    if "modelInput" in data:
        out["model_input"] = data["modelInput"]
    else:
        raise DeserializationError("StartAsyncInvokeRequest.model_input required")
    if "outputDataConfig" in data:
        import aws_sdk_bedrock_runtime.types.async_invoke_output_data_config

        out["output_data_config"] = (
            aws_sdk_bedrock_runtime.types.async_invoke_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartAsyncInvokeRequest.output_data_config required"
        )
    if "tags" in data:
        import aws_sdk_bedrock_runtime.types.tag_list

        out["tags"] = aws_sdk_bedrock_runtime.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
