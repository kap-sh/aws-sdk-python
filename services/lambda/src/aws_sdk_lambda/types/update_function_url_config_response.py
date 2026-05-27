"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateFunctionUrlConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.cors
    import aws_sdk_lambda.types.function_arn
    import aws_sdk_lambda.types.function_url
    import aws_sdk_lambda.types.function_url_auth_type
    import aws_sdk_lambda.types.invoke_mode
    import aws_sdk_lambda.types.timestamp


class UpdateFunctionUrlConfigResponse(TypedDict):
    function_url: "aws_sdk_lambda.types.function_url.FunctionUrl"
    """<p>The HTTP URL endpoint for your function.</p>"""
    function_arn: "aws_sdk_lambda.types.function_arn.FunctionArn"
    """<p>The Amazon Resource Name (ARN) of your function.</p>"""
    auth_type: "aws_sdk_lambda.types.function_url_auth_type.FunctionUrlAuthType"
    """<p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html\">Control access to Lambda function URLs</a>.</p>"""
    cors: NotRequired["aws_sdk_lambda.types.cors.Cors"]
    """<p>The <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS\">cross-origin resource sharing (CORS)</a> settings for your function URL.</p>"""
    creation_time: "aws_sdk_lambda.types.timestamp.Timestamp"
    """<p>When the function URL was created, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    last_modified_time: "aws_sdk_lambda.types.timestamp.Timestamp"
    """<p>When the function URL configuration was last updated, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    invoke_mode: NotRequired["aws_sdk_lambda.types.invoke_mode.InvokeMode"]
    """<p>Use one of the following options:</p> <ul> <li> <p> <code>BUFFERED</code> – This is the default option. Lambda invokes your function using the <code>Invoke</code> API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.</p> </li> <li> <p> <code>RESPONSE_STREAM</code> – Your function streams payload results as they become available. Lambda invokes your function using the <code>InvokeWithResponseStream</code> API operation. The maximum response payload size is 200 MB.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFunctionUrlConfigResponse) -> dict:
    out: dict = {}
    out["FunctionUrl"] = value["function_url"]
    out["FunctionArn"] = value["function_arn"]
    import aws_sdk_lambda.types.function_url_auth_type

    out["AuthType"] = aws_sdk_lambda.types.function_url_auth_type.serialize_json(
        value["auth_type"]
    )
    if "cors" in value:
        import aws_sdk_lambda.types.cors

        out["Cors"] = aws_sdk_lambda.types.cors.serialize_json(value["cors"])
    out["CreationTime"] = value["creation_time"]
    out["LastModifiedTime"] = value["last_modified_time"]
    if "invoke_mode" in value:
        import aws_sdk_lambda.types.invoke_mode

        out["InvokeMode"] = aws_sdk_lambda.types.invoke_mode.serialize_json(
            value["invoke_mode"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFunctionUrlConfigResponse:
    out: UpdateFunctionUrlConfigResponse = {}  # type: ignore[typeddict-item]
    if "FunctionUrl" in data:
        out["function_url"] = data["FunctionUrl"]
    else:
        raise DeserializationError(
            "UpdateFunctionUrlConfigResponse.function_url required"
        )
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    else:
        raise DeserializationError(
            "UpdateFunctionUrlConfigResponse.function_arn required"
        )
    if "AuthType" in data:
        import aws_sdk_lambda.types.function_url_auth_type

        out["auth_type"] = aws_sdk_lambda.types.function_url_auth_type.deserialize_json(
            data["AuthType"]
        )
    else:
        raise DeserializationError("UpdateFunctionUrlConfigResponse.auth_type required")
    if "Cors" in data:
        import aws_sdk_lambda.types.cors

        out["cors"] = aws_sdk_lambda.types.cors.deserialize_json(data["Cors"])
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    else:
        raise DeserializationError(
            "UpdateFunctionUrlConfigResponse.creation_time required"
        )
    if "LastModifiedTime" in data:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        raise DeserializationError(
            "UpdateFunctionUrlConfigResponse.last_modified_time required"
        )
    if "InvokeMode" in data:
        import aws_sdk_lambda.types.invoke_mode

        out["invoke_mode"] = aws_sdk_lambda.types.invoke_mode.deserialize_json(
            data["InvokeMode"]
        )
    return out
