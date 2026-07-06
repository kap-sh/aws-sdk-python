"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateDataProtectionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class CreateDataProtectionSettingsResponse(TypedDict, closed=True):
    data_protection_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the data protection settings resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataProtectionSettingsResponse) -> dict:
    out: dict = {}
    out["dataProtectionSettingsArn"] = value["data_protection_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateDataProtectionSettingsResponse:
    out: CreateDataProtectionSettingsResponse = {}  # type: ignore[typeddict-item]
    if "dataProtectionSettingsArn" in data:
        out["data_protection_settings_arn"] = data["dataProtectionSettingsArn"]
    else:
        raise DeserializationError(
            "CreateDataProtectionSettingsResponse.data_protection_settings_arn required"
        )
    return out
