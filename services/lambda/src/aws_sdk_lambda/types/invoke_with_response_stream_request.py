"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStreamRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.blob
    import aws_sdk_lambda.types.log_type
    import aws_sdk_lambda.types.namespaced_function_name
    import aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier
    import aws_sdk_lambda.types.response_streaming_invocation_type
    import aws_sdk_lambda.types.string
    import aws_sdk_lambda.types.tenant_id


class InvokeWithResponseStreamRequest(TypedDict):
    function_name: (
        "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName"
    )
    """<p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    invocation_type: NotRequired[
        "aws_sdk_lambda.types.response_streaming_invocation_type.ResponseStreamingInvocationType"
    ]
    """<p>Use one of the following options:</p> <ul> <li> <p> <code>RequestResponse</code> (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API operation response includes the function response and additional data.</p> </li> <li> <p> <code>DryRun</code> – Validate parameter values and verify that the IAM user or role has permission to invoke the function.</p> </li> </ul>"""
    log_type: NotRequired["aws_sdk_lambda.types.log_type.LogType"]
    """<p>Set to <code>Tail</code> to include the execution log in the response. Applies to synchronously invoked functions only.</p>"""
    client_context: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object.</p>"""
    qualifier: NotRequired[
        "aws_sdk_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
    ]
    """<p>The alias name.</p>"""
    payload: NotRequired["aws_sdk_lambda.types.blob.Blob"]
    """<p>The JSON that you want to provide to your Lambda function as input.</p> <p>You can enter the JSON directly. For example, <code>--payload '{ \"key\": \"value\" }'</code>. You can also specify a file path. For example, <code>--payload file://payload.json</code>.</p>"""
    tenant_id: NotRequired["aws_sdk_lambda.types.tenant_id.TenantId"]
    """<p>The identifier of the tenant in a multi-tenant Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeWithResponseStreamRequest) -> dict:
    out: dict = {}
    if "payload" in value:
        import aws_sdk_lambda.types.blob

        out["Payload"] = aws_sdk_lambda.types.blob.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> InvokeWithResponseStreamRequest:
    out: InvokeWithResponseStreamRequest = {}  # type: ignore[typeddict-item]
    if "Payload" in data:
        import aws_sdk_lambda.types.blob

        out["payload"] = aws_sdk_lambda.types.blob.deserialize_json(data["Payload"])
    return out
