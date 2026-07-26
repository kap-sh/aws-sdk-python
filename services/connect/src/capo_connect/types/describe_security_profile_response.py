"""Generated from Smithy shape ``com.amazonaws.connect#DescribeSecurityProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.security_profile


class DescribeSecurityProfileResponse(TypedDict, closed=True):
    security_profile: NotRequired["capo_connect.types.security_profile.SecurityProfile"]
    """<p>The security profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSecurityProfileResponse) -> dict:
    out: dict = {}
    if "security_profile" in value:
        import capo_connect.types.security_profile

        out["SecurityProfile"] = capo_connect.types.security_profile.serialize_json(
            value["security_profile"]
        )
    return out


def deserialize_json(data: dict) -> DescribeSecurityProfileResponse:
    out: DescribeSecurityProfileResponse = {}  # type: ignore[typeddict-item]
    if "SecurityProfile" in data:
        import capo_connect.types.security_profile

        out["security_profile"] = capo_connect.types.security_profile.deserialize_json(
            data["SecurityProfile"]
        )
    return out
