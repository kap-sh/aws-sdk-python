"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRuleBasedMatchesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.match_id_list
    import aws_sdk_customer_profiles.types.token


class ListRuleBasedMatchesResponse(TypedDict):
    match_ids: NotRequired["aws_sdk_customer_profiles.types.match_id_list.MatchIdList"]
    """<p>The list of <code>MatchIds</code> for the given domain.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous <code>ListRuleBasedMatches</code> API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuleBasedMatchesResponse) -> dict:
    out: dict = {}
    if "match_ids" in value:
        import aws_sdk_customer_profiles.types.match_id_list

        out["MatchIds"] = aws_sdk_customer_profiles.types.match_id_list.serialize_json(
            value["match_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRuleBasedMatchesResponse:
    out: ListRuleBasedMatchesResponse = {}  # type: ignore[typeddict-item]
    if "MatchIds" in data:
        import aws_sdk_customer_profiles.types.match_id_list

        out["match_ids"] = (
            aws_sdk_customer_profiles.types.match_id_list.deserialize_json(
                data["MatchIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
