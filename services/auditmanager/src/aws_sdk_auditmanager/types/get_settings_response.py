"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.settings


class GetSettingsResponse(TypedDict, closed=True):
    settings: NotRequired["aws_sdk_auditmanager.types.settings.Settings"]
    """<p> The settings object that holds all supported Audit Manager settings. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSettingsResponse) -> dict:
    out: dict = {}
    if "settings" in value:
        import aws_sdk_auditmanager.types.settings

        out["settings"] = aws_sdk_auditmanager.types.settings.serialize_json(
            value["settings"]
        )
    return out


def deserialize_json(data: dict) -> GetSettingsResponse:
    out: GetSettingsResponse = {}  # type: ignore[typeddict-item]
    if "settings" in data:
        import aws_sdk_auditmanager.types.settings

        out["settings"] = aws_sdk_auditmanager.types.settings.deserialize_json(
            data["settings"]
        )
    return out
