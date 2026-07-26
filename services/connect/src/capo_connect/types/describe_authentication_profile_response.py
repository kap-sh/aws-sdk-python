"""Generated from Smithy shape ``com.amazonaws.connect#DescribeAuthenticationProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.authentication_profile


class DescribeAuthenticationProfileResponse(TypedDict, closed=True):
    authentication_profile: NotRequired[
        "capo_connect.types.authentication_profile.AuthenticationProfile"
    ]
    """<p>The authentication profile object being described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuthenticationProfileResponse) -> dict:
    out: dict = {}
    if "authentication_profile" in value:
        import capo_connect.types.authentication_profile

        out["AuthenticationProfile"] = (
            capo_connect.types.authentication_profile.serialize_json(
                value["authentication_profile"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAuthenticationProfileResponse:
    out: DescribeAuthenticationProfileResponse = {}  # type: ignore[typeddict-item]
    if "AuthenticationProfile" in data:
        import capo_connect.types.authentication_profile

        out["authentication_profile"] = (
            capo_connect.types.authentication_profile.deserialize_json(
                data["AuthenticationProfile"]
            )
        )
    return out
