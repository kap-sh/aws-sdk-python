"""Generated from Smithy shape ``com.amazonaws.route53profiles#ListProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.next_token
    import aws_sdk_route53profiles.types.profile_summary_list


class ListProfilesResponse(TypedDict):
    profile_summaries: NotRequired[
        "aws_sdk_route53profiles.types.profile_summary_list.ProfileSummaryList"
    ]
    """<p> Summary information about the Profiles. </p>"""
    next_token: NotRequired["aws_sdk_route53profiles.types.next_token.NextToken"]
    """<p> If more than <code>MaxResults</code> resource associations match the specified criteria, you can submit another <code>ListProfiles</code> request to get the next group of results. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfilesResponse) -> dict:
    out: dict = {}
    if "profile_summaries" in value:
        import aws_sdk_route53profiles.types.profile_summary_list

        out["ProfileSummaries"] = (
            aws_sdk_route53profiles.types.profile_summary_list.serialize_json(
                value["profile_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfilesResponse:
    out: ListProfilesResponse = {}  # type: ignore[typeddict-item]
    if "ProfileSummaries" in data:
        import aws_sdk_route53profiles.types.profile_summary_list

        out["profile_summaries"] = (
            aws_sdk_route53profiles.types.profile_summary_list.deserialize_json(
                data["ProfileSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
