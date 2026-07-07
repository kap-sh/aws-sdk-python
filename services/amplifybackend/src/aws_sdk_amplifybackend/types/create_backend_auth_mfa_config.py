"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendAuthMFAConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.mfa_mode
    import aws_sdk_amplifybackend.types.settings


class CreateBackendAuthMFAConfig(TypedDict, closed=True):
    mfa_mode: NotRequired["aws_sdk_amplifybackend.types.mfa_mode.MFAMode"]
    """<p>Describes whether MFA should be [ON, OFF, or OPTIONAL] for authentication in your Amplify project.</p>"""
    settings: NotRequired["aws_sdk_amplifybackend.types.settings.Settings"]
    """<p>Describes the configuration settings and methods for your Amplify app users to use MFA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendAuthMFAConfig) -> dict:
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


def deserialize_json(data: dict) -> CreateBackendAuthMFAConfig:
    out: CreateBackendAuthMFAConfig = {}  # type: ignore[typeddict-item]
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
