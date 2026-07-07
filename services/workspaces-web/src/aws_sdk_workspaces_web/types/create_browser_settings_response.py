"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateBrowserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class CreateBrowserSettingsResponse(TypedDict, closed=True):
    browser_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the browser settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrowserSettingsResponse) -> dict:
    out: dict = {}
    out["browserSettingsArn"] = value["browser_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateBrowserSettingsResponse:
    out: CreateBrowserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "browserSettingsArn" in data:
        out["browser_settings_arn"] = data["browserSettingsArn"]
    else:
        raise DeserializationError(
            "CreateBrowserSettingsResponse.browser_settings_arn required"
        )
    return out
