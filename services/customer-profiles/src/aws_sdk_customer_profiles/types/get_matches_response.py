"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetMatchesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.matches_list
    import aws_sdk_customer_profiles.types.matches_number
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.token


class GetMatchesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    match_generation_date: NotRequired[
        "aws_sdk_customer_profiles.types.timestamp.timestamp"
    ]
    """<p>The timestamp this version of Match Result generated.</p>"""
    potential_matches: NotRequired[
        "aws_sdk_customer_profiles.types.matches_number.matchesNumber"
    ]
    """<p>The number of potential matches found.</p>"""
    matches: NotRequired["aws_sdk_customer_profiles.types.matches_list.MatchesList"]
    """<p>The list of matched profiles for this instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMatchesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "match_generation_date" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["MatchGenerationDate"] = (
            aws_sdk_customer_profiles.types.timestamp.serialize_json(
                value["match_generation_date"]
            )
        )
    if "potential_matches" in value:
        out["PotentialMatches"] = value["potential_matches"]
    if "matches" in value:
        import aws_sdk_customer_profiles.types.matches_list

        out["Matches"] = aws_sdk_customer_profiles.types.matches_list.serialize_json(
            value["matches"]
        )
    return out


def deserialize_json(data: dict) -> GetMatchesResponse:
    out: GetMatchesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MatchGenerationDate" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["match_generation_date"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["MatchGenerationDate"]
            )
        )
    if "PotentialMatches" in data:
        out["potential_matches"] = data["PotentialMatches"]
    if "Matches" in data:
        import aws_sdk_customer_profiles.types.matches_list

        out["matches"] = aws_sdk_customer_profiles.types.matches_list.deserialize_json(
            data["Matches"]
        )
    return out
