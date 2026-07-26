"""Generated from Smithy shape ``com.amazonaws.iot#DeleteSecurityProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.optional_version
    import capo_iot.types.security_profile_name


class DeleteSecurityProfileRequest(TypedDict, closed=True):
    security_profile_name: "capo_iot.types.security_profile_name.SecurityProfileName"
    """<p>The name of the security profile to be deleted.</p>"""
    expected_version: NotRequired["capo_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the security profile. A new version is generated whenever the security profile is updated. If you specify a value that is different from the actual version, a <code>VersionConflictException</code> is thrown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSecurityProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSecurityProfileRequest:
    out: DeleteSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    return out
