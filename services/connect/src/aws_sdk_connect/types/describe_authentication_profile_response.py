"""Generated from Smithy shape ``com.amazonaws.connect#DescribeAuthenticationProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.authentication_profile


class DescribeAuthenticationProfileResponse(TypedDict):
    authentication_profile: NotRequired[
        "aws_sdk_connect.types.authentication_profile.AuthenticationProfile"
    ]
    """<p>The authentication profile object being described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuthenticationProfileResponse) -> dict:
    out: dict = {}
    if "authentication_profile" in value:
        import aws_sdk_connect.types.authentication_profile

        out["AuthenticationProfile"] = (
            aws_sdk_connect.types.authentication_profile.serialize_json(
                value["authentication_profile"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAuthenticationProfileResponse:
    out: DescribeAuthenticationProfileResponse = {}  # type: ignore[typeddict-item]
    if "AuthenticationProfile" in data:
        import aws_sdk_connect.types.authentication_profile

        out["authentication_profile"] = (
            aws_sdk_connect.types.authentication_profile.deserialize_json(
                data["AuthenticationProfile"]
            )
        )
    return out
