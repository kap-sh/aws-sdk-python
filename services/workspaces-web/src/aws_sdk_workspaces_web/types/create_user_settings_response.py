"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateUserSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class CreateUserSettingsResponse(TypedDict):
    user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserSettingsResponse) -> dict:
    out: dict = {}
    out["userSettingsArn"] = value["user_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateUserSettingsResponse:
    out: CreateUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "userSettingsArn" in data:
        out["user_settings_arn"] = data["userSettingsArn"]
    else:
        raise DeserializationError(
            "CreateUserSettingsResponse.user_settings_arn required"
        )
    return out
