"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.settings


class UpdateSettingsResponse(TypedDict):
    settings: NotRequired["aws_sdk_auditmanager.types.settings.Settings"]
    """<p> The current list of settings. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSettingsResponse) -> dict:
    out: dict = {}
    if "settings" in value:
        import aws_sdk_auditmanager.types.settings

        out["settings"] = aws_sdk_auditmanager.types.settings.serialize_json(
            value["settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSettingsResponse:
    out: UpdateSettingsResponse = {}  # type: ignore[typeddict-item]
    if "settings" in data:
        import aws_sdk_auditmanager.types.settings

        out["settings"] = aws_sdk_auditmanager.types.settings.deserialize_json(
            data["settings"]
        )
    return out
