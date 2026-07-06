"""Generated from Smithy shape ``com.amazonaws.connect#SearchSecurityProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.next_token2500
    import aws_sdk_connect.types.security_profiles_search_summary_list


class SearchSecurityProfilesResponse(TypedDict, closed=True):
    security_profiles: NotRequired[
        "aws_sdk_connect.types.security_profiles_search_summary_list.SecurityProfilesSearchSummaryList"
    ]
    """<p>Information about the security profiles.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of security profiles which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSecurityProfilesResponse) -> dict:
    out: dict = {}
    if "security_profiles" in value:
        import aws_sdk_connect.types.security_profiles_search_summary_list

        out["SecurityProfiles"] = (
            aws_sdk_connect.types.security_profiles_search_summary_list.serialize_json(
                value["security_profiles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchSecurityProfilesResponse:
    out: SearchSecurityProfilesResponse = {}  # type: ignore[typeddict-item]
    if "SecurityProfiles" in data:
        import aws_sdk_connect.types.security_profiles_search_summary_list

        out["security_profiles"] = (
            aws_sdk_connect.types.security_profiles_search_summary_list.deserialize_json(
                data["SecurityProfiles"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
