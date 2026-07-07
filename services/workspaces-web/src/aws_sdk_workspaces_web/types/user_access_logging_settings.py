"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UserAccessLoggingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.arn_list
    import aws_sdk_workspaces_web.types.kinesis_stream_arn


class UserAccessLoggingSettings(TypedDict, closed=True):
    user_access_logging_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user access logging settings.</p>"""
    associated_portal_arns: NotRequired["aws_sdk_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this user access logging settings is associated with.</p>"""
    kinesis_stream_arn: NotRequired[
        "aws_sdk_workspaces_web.types.kinesis_stream_arn.KinesisStreamArn"
    ]
    """<p>The ARN of the Kinesis stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessLoggingSettings) -> dict:
    out: dict = {}
    out["userAccessLoggingSettingsArn"] = value["user_access_logging_settings_arn"]
    if "associated_portal_arns" in value:
        import aws_sdk_workspaces_web.types.arn_list

        out["associatedPortalArns"] = (
            aws_sdk_workspaces_web.types.arn_list.serialize_json(
                value["associated_portal_arns"]
            )
        )
    if "kinesis_stream_arn" in value:
        out["kinesisStreamArn"] = value["kinesis_stream_arn"]
    return out


def deserialize_json(data: dict) -> UserAccessLoggingSettings:
    out: UserAccessLoggingSettings = {}  # type: ignore[typeddict-item]
    if "userAccessLoggingSettingsArn" in data:
        out["user_access_logging_settings_arn"] = data["userAccessLoggingSettingsArn"]
    else:
        raise DeserializationError(
            "UserAccessLoggingSettings.user_access_logging_settings_arn required"
        )
    if "associatedPortalArns" in data:
        import aws_sdk_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            aws_sdk_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if "kinesisStreamArn" in data:
        out["kinesis_stream_arn"] = data["kinesisStreamArn"]
    return out
