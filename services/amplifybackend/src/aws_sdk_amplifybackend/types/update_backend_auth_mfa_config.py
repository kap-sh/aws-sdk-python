"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthMFAConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.mfa_mode
    import aws_sdk_amplifybackend.types.settings


class UpdateBackendAuthMFAConfig(TypedDict):
    mfa_mode: NotRequired["aws_sdk_amplifybackend.types.mfa_mode.MFAMode"]
    """<p>The MFA mode for the backend of your Amplify project.</p>"""
    settings: NotRequired["aws_sdk_amplifybackend.types.settings.Settings"]
    """<p>The settings of your MFA configuration for the backend of your Amplify project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthMFAConfig) -> dict:
    out: dict = {}
    if "mfa_mode" in value:
        import aws_sdk_amplifybackend.types.mfa_mode

        out["MFAMode"] = aws_sdk_amplifybackend.types.mfa_mode.serialize_json(
            value["mfa_mode"]
        )
    if "settings" in value:
        import aws_sdk_amplifybackend.types.settings

        out["settings"] = aws_sdk_amplifybackend.types.settings.serialize_json(
            value["settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthMFAConfig:
    out: UpdateBackendAuthMFAConfig = {}  # type: ignore[typeddict-item]
    if "MFAMode" in data:
        import aws_sdk_amplifybackend.types.mfa_mode

        out["mfa_mode"] = aws_sdk_amplifybackend.types.mfa_mode.deserialize_json(
            data["MFAMode"]
        )
    if "settings" in data:
        import aws_sdk_amplifybackend.types.settings

        out["settings"] = aws_sdk_amplifybackend.types.settings.deserialize_json(
            data["settings"]
        )
    return out
