"""Generated from Smithy shape ``com.amazonaws.shield#ListAttacksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.attack_summaries
    import aws_sdk_shield.types.token


class ListAttacksResponse(TypedDict, closed=True):
    attack_summaries: NotRequired[
        "aws_sdk_shield.types.attack_summaries.AttackSummaries"
    ]
    """<p>The attack information for the specified time range.</p>"""
    next_token: NotRequired["aws_sdk_shield.types.token.Token"]
    """<p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAttacksResponse) -> dict:
    out: dict = {}
    if "attack_summaries" in value:
        import aws_sdk_shield.types.attack_summaries

        out["AttackSummaries"] = (
            aws_sdk_shield.types.attack_summaries.serialize_aws_json_1_1(
                value["attack_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAttacksResponse:
    out: ListAttacksResponse = {}  # type: ignore[typeddict-item]
    if "AttackSummaries" in data:
        import aws_sdk_shield.types.attack_summaries

        out["attack_summaries"] = (
            aws_sdk_shield.types.attack_summaries.deserialize_aws_json_1_1(
                data["AttackSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
