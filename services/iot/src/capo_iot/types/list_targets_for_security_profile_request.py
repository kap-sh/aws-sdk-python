"""Generated from Smithy shape ``com.amazonaws.iot#ListTargetsForSecurityProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.max_results
    import capo_iot.types.next_token
    import capo_iot.types.security_profile_name


class ListTargetsForSecurityProfileRequest(TypedDict, closed=True):
    security_profile_name: "capo_iot.types.security_profile_name.SecurityProfileName"
    """<p>The security profile.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsForSecurityProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTargetsForSecurityProfileRequest:
    out: ListTargetsForSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    return out
