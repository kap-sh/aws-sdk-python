"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateBrowserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class AssociateBrowserSettingsResponse(TypedDict, closed=True):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    browser_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the browser settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateBrowserSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["browserSettingsArn"] = value["browser_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateBrowserSettingsResponse:
    out: AssociateBrowserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError(
            "AssociateBrowserSettingsResponse.portal_arn required"
        )
    if "browserSettingsArn" in data:
        out["browser_settings_arn"] = data["browserSettingsArn"]
    else:
        raise DeserializationError(
            "AssociateBrowserSettingsResponse.browser_settings_arn required"
        )
    return out
