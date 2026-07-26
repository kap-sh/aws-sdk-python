"""Generated from Smithy shape ``com.amazonaws.route53profiles#GetProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.profile


class GetProfileResponse(TypedDict, closed=True):
    profile: NotRequired["capo_route53profiles.types.profile.Profile"]
    """<p> Information about the Profile, including the status of the Profile. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileResponse) -> dict:
    out: dict = {}
    if "profile" in value:
        import capo_route53profiles.types.profile

        out["Profile"] = capo_route53profiles.types.profile.serialize_json(
            value["profile"]
        )
    return out


def deserialize_json(data: dict) -> GetProfileResponse:
    out: GetProfileResponse = {}  # type: ignore[typeddict-item]
    if "Profile" in data:
        import capo_route53profiles.types.profile

        out["profile"] = capo_route53profiles.types.profile.deserialize_json(
            data["Profile"]
        )
    return out
