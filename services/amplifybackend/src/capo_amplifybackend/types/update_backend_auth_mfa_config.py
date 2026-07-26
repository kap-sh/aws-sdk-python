"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthMFAConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.mfa_mode
    import capo_amplifybackend.types.settings


class UpdateBackendAuthMFAConfig(TypedDict, closed=True):
    mfa_mode: NotRequired["capo_amplifybackend.types.mfa_mode.MFAMode"]
    """<p>The MFA mode for the backend of your Amplify project.</p>"""
    settings: NotRequired["capo_amplifybackend.types.settings.Settings"]
    """<p>The settings of your MFA configuration for the backend of your Amplify project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthMFAConfig) -> dict:
    out: dict = {}
    if "mfa_mode" in value:
        import capo_amplifybackend.types.mfa_mode

        out["MFAMode"] = capo_amplifybackend.types.mfa_mode.serialize_json(
            value["mfa_mode"]
        )
    if "settings" in value:
        import capo_amplifybackend.types.settings

        out["settings"] = capo_amplifybackend.types.settings.serialize_json(
            value["settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthMFAConfig:
    out: UpdateBackendAuthMFAConfig = {}  # type: ignore[typeddict-item]
    if "MFAMode" in data:
        import capo_amplifybackend.types.mfa_mode

        out["mfa_mode"] = capo_amplifybackend.types.mfa_mode.deserialize_json(
            data["MFAMode"]
        )
    if "settings" in data:
        import capo_amplifybackend.types.settings

        out["settings"] = capo_amplifybackend.types.settings.deserialize_json(
            data["settings"]
        )
    return out
