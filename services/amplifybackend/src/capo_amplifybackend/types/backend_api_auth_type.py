"""Generated from Smithy shape ``com.amazonaws.amplifybackend#BackendAPIAuthType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.backend_api_app_sync_auth_settings
    import capo_amplifybackend.types.mode


class BackendAPIAuthType(TypedDict, closed=True):
    mode: NotRequired["capo_amplifybackend.types.mode.Mode"]
    """<p>Describes the authentication mode.</p>"""
    settings: NotRequired[
        "capo_amplifybackend.types.backend_api_app_sync_auth_settings.BackendAPIAppSyncAuthSettings"
    ]
    """<p>Describes settings for the authentication mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendAPIAuthType) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_amplifybackend.types.mode

        out["mode"] = capo_amplifybackend.types.mode.serialize_json(value["mode"])
    if "settings" in value:
        import capo_amplifybackend.types.backend_api_app_sync_auth_settings

        out["settings"] = (
            capo_amplifybackend.types.backend_api_app_sync_auth_settings.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> BackendAPIAuthType:
    out: BackendAPIAuthType = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import capo_amplifybackend.types.mode

        out["mode"] = capo_amplifybackend.types.mode.deserialize_json(data["mode"])
    if "settings" in data:
        import capo_amplifybackend.types.backend_api_app_sync_auth_settings

        out["settings"] = (
            capo_amplifybackend.types.backend_api_app_sync_auth_settings.deserialize_json(
                data["settings"]
            )
        )
    return out
