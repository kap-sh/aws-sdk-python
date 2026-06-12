"""Generated from Smithy shape ``com.amazonaws.iot#ListTargetsForSecurityProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.security_profile_name


class ListTargetsForSecurityProfileRequest(TypedDict):
    security_profile_name: "aws_sdk_iot.types.security_profile_name.SecurityProfileName"
    """<p>The security profile.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsForSecurityProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTargetsForSecurityProfileRequest:
    out: ListTargetsForSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    return out
