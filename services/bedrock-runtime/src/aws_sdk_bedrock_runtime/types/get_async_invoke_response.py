"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GetAsyncInvokeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.async_invoke_arn
    import aws_sdk_bedrock_runtime.types.async_invoke_idempotency_token
    import aws_sdk_bedrock_runtime.types.async_invoke_message
    import aws_sdk_bedrock_runtime.types.async_invoke_output_data_config
    import aws_sdk_bedrock_runtime.types.async_invoke_status
    import aws_sdk_bedrock_runtime.types.invocation_arn
    import aws_sdk_bedrock_runtime.types.timestamp


class GetAsyncInvokeResponse(TypedDict):
    invocation_arn: "aws_sdk_bedrock_runtime.types.invocation_arn.InvocationArn"
    """<p>The invocation's ARN.</p>"""
    model_arn: "aws_sdk_bedrock_runtime.types.async_invoke_arn.AsyncInvokeArn"
    """<p>The invocation's model ARN.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock_runtime.types.async_invoke_idempotency_token.AsyncInvokeIdempotencyToken"
    ]
    """<p>The invocation's idempotency token.</p>"""
    status: "aws_sdk_bedrock_runtime.types.async_invoke_status.AsyncInvokeStatus"
    """<p>The invocation's status.</p>"""
    failure_message: NotRequired[
        "aws_sdk_bedrock_runtime.types.async_invoke_message.AsyncInvokeMessage"
    ]
    """<p>An error message.</p>"""
    submit_time: "aws_sdk_bedrock_runtime.types.timestamp.Timestamp"
    """<p>When the invocation request was submitted.</p>"""
    last_modified_time: NotRequired["aws_sdk_bedrock_runtime.types.timestamp.Timestamp"]
    """<p>The invocation's last modified time.</p>"""
    end_time: NotRequired["aws_sdk_bedrock_runtime.types.timestamp.Timestamp"]
    """<p>When the invocation ended.</p>"""
    output_data_config: "aws_sdk_bedrock_runtime.types.async_invoke_output_data_config.AsyncInvokeOutputDataConfig"
    """<p>Output data settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAsyncInvokeResponse) -> dict:
    out: dict = {}
    out["invocationArn"] = value["invocation_arn"]
    out["modelArn"] = value["model_arn"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    import aws_sdk_bedrock_runtime.types.async_invoke_status

    out["status"] = aws_sdk_bedrock_runtime.types.async_invoke_status.serialize_json(
        value["status"]
    )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    import aws_sdk_bedrock_runtime.types.timestamp

    out["submitTime"] = aws_sdk_bedrock_runtime.types.timestamp.serialize_json(
        value["submit_time"]
    )
    if "last_modified_time" in value:
        import aws_sdk_bedrock_runtime.types.timestamp

        out["lastModifiedTime"] = (
            aws_sdk_bedrock_runtime.types.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_bedrock_runtime.types.timestamp

        out["endTime"] = aws_sdk_bedrock_runtime.types.timestamp.serialize_json(
            value["end_time"]
        )
    import aws_sdk_bedrock_runtime.types.async_invoke_output_data_config

    out["outputDataConfig"] = (
        aws_sdk_bedrock_runtime.types.async_invoke_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAsyncInvokeResponse:
    out: GetAsyncInvokeResponse = {}  # type: ignore[typeddict-item]
    if "invocationArn" in data:
        out["invocation_arn"] = data["invocationArn"]
    else:
        raise DeserializationError("GetAsyncInvokeResponse.invocation_arn required")
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("GetAsyncInvokeResponse.model_arn required")
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "status" in data:
        import aws_sdk_bedrock_runtime.types.async_invoke_status

        out["status"] = (
            aws_sdk_bedrock_runtime.types.async_invoke_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetAsyncInvokeResponse.status required")
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "submitTime" in data:
        import aws_sdk_bedrock_runtime.types.timestamp

        out["submit_time"] = aws_sdk_bedrock_runtime.types.timestamp.deserialize_json(
            data["submitTime"]
        )
    else:
        raise DeserializationError("GetAsyncInvokeResponse.submit_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock_runtime.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_bedrock_runtime.types.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_bedrock_runtime.types.timestamp

        out["end_time"] = aws_sdk_bedrock_runtime.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if "outputDataConfig" in data:
        import aws_sdk_bedrock_runtime.types.async_invoke_output_data_config

        out["output_data_config"] = (
            aws_sdk_bedrock_runtime.types.async_invoke_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError("GetAsyncInvokeResponse.output_data_config required")
    return out
