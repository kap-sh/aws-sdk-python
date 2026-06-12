"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ConversationLogsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.iam_role_arn
    import aws_sdk_lex_model_building_service.types.log_settings_response_list


class ConversationLogsResponse(TypedDict):
    log_settings: NotRequired[
        "aws_sdk_lex_model_building_service.types.log_settings_response_list.LogSettingsResponseList"
    ]
    """<p>The settings for your conversation logs. You can log text, audio, or both.</p>"""
    iam_role_arn: NotRequired[
        "aws_sdk_lex_model_building_service.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role used to write your logs to CloudWatch Logs or an S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLogsResponse) -> dict:
    out: dict = {}
    if "log_settings" in value:
        import aws_sdk_lex_model_building_service.types.log_settings_response_list

        out["logSettings"] = (
            aws_sdk_lex_model_building_service.types.log_settings_response_list.serialize_json(
                value["log_settings"]
            )
        )
    if "iam_role_arn" in value:
        out["iamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_json(data: dict) -> ConversationLogsResponse:
    out: ConversationLogsResponse = {}  # type: ignore[typeddict-item]
    if "logSettings" in data:
        import aws_sdk_lex_model_building_service.types.log_settings_response_list

        out["log_settings"] = (
            aws_sdk_lex_model_building_service.types.log_settings_response_list.deserialize_json(
                data["logSettings"]
            )
        )
    if "iamRoleArn" in data:
        out["iam_role_arn"] = data["iamRoleArn"]
    return out
