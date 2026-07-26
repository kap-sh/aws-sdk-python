"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateRecommenderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class UpdateRecommenderResponse(TypedDict, closed=True):
    recommender_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The same recommender Amazon Resource Name (ARN) as given in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRecommenderResponse) -> dict:
    out: dict = {}
    if "recommender_arn" in value:
        out["recommenderArn"] = value["recommender_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRecommenderResponse:
    out: UpdateRecommenderResponse = {}  # type: ignore[typeddict-item]
    if "recommenderArn" in data:
        out["recommender_arn"] = data["recommenderArn"]
    return out
