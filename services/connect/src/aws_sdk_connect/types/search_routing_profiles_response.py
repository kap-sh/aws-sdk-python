"""Generated from Smithy shape ``com.amazonaws.connect#SearchRoutingProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.next_token2500
    import aws_sdk_connect.types.routing_profile_list


class SearchRoutingProfilesResponse(TypedDict, closed=True):
    routing_profiles: NotRequired[
        "aws_sdk_connect.types.routing_profile_list.RoutingProfileList"
    ]
    """<p>Information about the routing profiles.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of routing profiles which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRoutingProfilesResponse) -> dict:
    out: dict = {}
    if "routing_profiles" in value:
        import aws_sdk_connect.types.routing_profile_list

        out["RoutingProfiles"] = (
            aws_sdk_connect.types.routing_profile_list.serialize_json(
                value["routing_profiles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchRoutingProfilesResponse:
    out: SearchRoutingProfilesResponse = {}  # type: ignore[typeddict-item]
    if "RoutingProfiles" in data:
        import aws_sdk_connect.types.routing_profile_list

        out["routing_profiles"] = (
            aws_sdk_connect.types.routing_profile_list.deserialize_json(
                data["RoutingProfiles"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
