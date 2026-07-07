"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteDataProtectionSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class DeleteDataProtectionSettingsRequest(TypedDict, closed=True):
    data_protection_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the data protection settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataProtectionSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataProtectionSettingsRequest:
    out: DeleteDataProtectionSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
