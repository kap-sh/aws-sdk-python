"""Generated from Smithy shape ``com.amazonaws.personalize#ListRecommendersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.next_token
    import capo_personalize.types.recommenders


class ListRecommendersResponse(TypedDict, closed=True):
    recommenders: NotRequired["capo_personalize.types.recommenders.Recommenders"]
    """<p>A list of the recommenders.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of recommenders (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRecommendersResponse) -> dict:
    out: dict = {}
    if "recommenders" in value:
        import capo_personalize.types.recommenders

        out["recommenders"] = (
            capo_personalize.types.recommenders.serialize_aws_json_1_1(
                value["recommenders"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRecommendersResponse:
    out: ListRecommendersResponse = {}  # type: ignore[typeddict-item]
    if "recommenders" in data:
        import capo_personalize.types.recommenders

        out["recommenders"] = (
            capo_personalize.types.recommenders.deserialize_aws_json_1_1(
                data["recommenders"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
