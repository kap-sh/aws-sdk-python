"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#CodeHook``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.lambda_arn
    import aws_sdk_lex_model_building_service.types.message_version


class CodeHook(TypedDict):
    uri: "aws_sdk_lex_model_building_service.types.lambda_arn.LambdaARN"
    """<p>The Amazon Resource Name (ARN) of the Lambda function.</p>"""
    message_version: (
        "aws_sdk_lex_model_building_service.types.message_version.MessageVersion"
    )
    """<p>The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see <a>using-lambda</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeHook) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    out["messageVersion"] = value["message_version"]
    return out


def deserialize_json(data: dict) -> CodeHook:
    out: CodeHook = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("CodeHook.uri required")
    if "messageVersion" in data:
        out["message_version"] = data["messageVersion"]
    else:
        raise DeserializationError("CodeHook.message_version required")
    return out
