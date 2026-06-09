"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionCodeSigningConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.code_signing_config_arn
    import aws_sdk_lambda.types.function_name


class GetFunctionCodeSigningConfigResponse(TypedDict):
    code_signing_config_arn: (
        "aws_sdk_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>"""
    function_name: "aws_sdk_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionCodeSigningConfigResponse) -> dict:
    out: dict = {}
    out["CodeSigningConfigArn"] = value["code_signing_config_arn"]
    out["FunctionName"] = value["function_name"]
    return out


def deserialize_json(data: dict) -> GetFunctionCodeSigningConfigResponse:
    out: GetFunctionCodeSigningConfigResponse = {}  # type: ignore[typeddict-item]
    if "CodeSigningConfigArn" in data:
        out["code_signing_config_arn"] = data["CodeSigningConfigArn"]
    else:
        raise DeserializationError(
            "GetFunctionCodeSigningConfigResponse.code_signing_config_arn required"
        )
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError(
            "GetFunctionCodeSigningConfigResponse.function_name required"
        )
    return out
