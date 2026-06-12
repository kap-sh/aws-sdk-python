"""Generated from Smithy shape ``com.amazonaws.route53profiles#CreateProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.profile


class CreateProfileResponse(TypedDict):
    profile: NotRequired["aws_sdk_route53profiles.types.profile.Profile"]
    """<p> The Profile that you just created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileResponse) -> dict:
    out: dict = {}
    if "profile" in value:
        import aws_sdk_route53profiles.types.profile

        out["Profile"] = aws_sdk_route53profiles.types.profile.serialize_json(
            value["profile"]
        )
    return out


def deserialize_json(data: dict) -> CreateProfileResponse:
    out: CreateProfileResponse = {}  # type: ignore[typeddict-item]
    if "Profile" in data:
        import aws_sdk_route53profiles.types.profile

        out["profile"] = aws_sdk_route53profiles.types.profile.deserialize_json(
            data["Profile"]
        )
    return out
