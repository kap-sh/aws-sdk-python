"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ProfileDetailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.profile_detail


class ProfileDetailResponse(TypedDict, closed=True):
    profile: NotRequired["aws_sdk_rolesanywhere.types.profile_detail.ProfileDetail"]
    """<p>The state of the profile after a read or write operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileDetailResponse) -> dict:
    out: dict = {}
    if "profile" in value:
        import aws_sdk_rolesanywhere.types.profile_detail

        out["profile"] = aws_sdk_rolesanywhere.types.profile_detail.serialize_json(
            value["profile"]
        )
    return out


def deserialize_json(data: dict) -> ProfileDetailResponse:
    out: ProfileDetailResponse = {}  # type: ignore[typeddict-item]
    if "profile" in data:
        import aws_sdk_rolesanywhere.types.profile_detail

        out["profile"] = aws_sdk_rolesanywhere.types.profile_detail.deserialize_json(
            data["profile"]
        )
    return out
