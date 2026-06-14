"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UserAccessLoggingSettingsSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.kinesis_stream_arn


class UserAccessLoggingSettingsSummary(TypedDict):
    user_access_logging_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user access logging settings.</p>"""
    kinesis_stream_arn: NotRequired[
        "aws_sdk_workspaces_web.types.kinesis_stream_arn.KinesisStreamArn"
    ]
    """<p>The ARN of the Kinesis stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessLoggingSettingsSummary) -> dict:
    out: dict = {}
    out["userAccessLoggingSettingsArn"] = value["user_access_logging_settings_arn"]
    if "kinesis_stream_arn" in value:
        out["kinesisStreamArn"] = value["kinesis_stream_arn"]
    return out


def deserialize_json(data: dict) -> UserAccessLoggingSettingsSummary:
    out: UserAccessLoggingSettingsSummary = {}  # type: ignore[typeddict-item]
    if "userAccessLoggingSettingsArn" in data:
        out["user_access_logging_settings_arn"] = data["userAccessLoggingSettingsArn"]
    else:
        raise DeserializationError(
            "UserAccessLoggingSettingsSummary.user_access_logging_settings_arn required"
        )
    if "kinesisStreamArn" in data:
        out["kinesis_stream_arn"] = data["kinesisStreamArn"]
    return out
