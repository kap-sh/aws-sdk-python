"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSimilarProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.double
    import aws_sdk_customer_profiles.types.match_type
    import aws_sdk_customer_profiles.types.profile_id_list
    import aws_sdk_customer_profiles.types.rule_level
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.token


class GetSimilarProfilesResponse(TypedDict):
    profile_ids: NotRequired[
        "aws_sdk_customer_profiles.types.profile_id_list.ProfileIdList"
    ]
    """<p>Set of <code>profileId</code>s that belong to the same matching group.</p>"""
    match_id: NotRequired["aws_sdk_customer_profiles.types.string1_to255.string1To255"]
    """<p>The string <code>matchId</code> that the similar profiles belong to.</p>"""
    match_type: NotRequired["aws_sdk_customer_profiles.types.match_type.MatchType"]
    """<p>Specify the type of matching to get similar profiles for.</p>"""
    rule_level: NotRequired["aws_sdk_customer_profiles.types.rule_level.RuleLevel"]
    """<p>The integer rule level that the profiles matched on.</p>"""
    confidence_score: NotRequired["aws_sdk_customer_profiles.types.double.Double"]
    """<p>It only has value when the <code>MatchType</code> is <code>ML_BASED_MATCHING</code>.A number between 0 and 1, where a higher score means higher similarity. Examining match confidence scores lets you distinguish between groups of similar records in which the system is highly confident (which you may decide to merge), groups of similar records about which the system is uncertain (which you may decide to have reviewed by a human), and groups of similar records that the system deems to be unlikely (which you may decide to reject). Given confidence scores vary as per the data input, it should not be used as an absolute measure of matching quality.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous <code>GetSimilarProfiles</code> API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSimilarProfilesResponse) -> dict:
    out: dict = {}
    if "profile_ids" in value:
        import aws_sdk_customer_profiles.types.profile_id_list

        out["ProfileIds"] = (
            aws_sdk_customer_profiles.types.profile_id_list.serialize_json(
                value["profile_ids"]
            )
        )
    if "match_id" in value:
        out["MatchId"] = value["match_id"]
    if "match_type" in value:
        import aws_sdk_customer_profiles.types.match_type

        out["MatchType"] = aws_sdk_customer_profiles.types.match_type.serialize_json(
            value["match_type"]
        )
    if "rule_level" in value:
        out["RuleLevel"] = value["rule_level"]
    if "confidence_score" in value:
        out["ConfidenceScore"] = value["confidence_score"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSimilarProfilesResponse:
    out: GetSimilarProfilesResponse = {}  # type: ignore[typeddict-item]
    if "ProfileIds" in data:
        import aws_sdk_customer_profiles.types.profile_id_list

        out["profile_ids"] = (
            aws_sdk_customer_profiles.types.profile_id_list.deserialize_json(
                data["ProfileIds"]
            )
        )
    if "MatchId" in data:
        out["match_id"] = data["MatchId"]
    if "MatchType" in data:
        import aws_sdk_customer_profiles.types.match_type

        out["match_type"] = aws_sdk_customer_profiles.types.match_type.deserialize_json(
            data["MatchType"]
        )
    if "RuleLevel" in data:
        out["rule_level"] = data["RuleLevel"]
    if "ConfidenceScore" in data:
        out["confidence_score"] = data["ConfidenceScore"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
