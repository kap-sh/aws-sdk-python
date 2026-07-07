"""Generated from Smithy shape ``com.amazonaws.personalize#StopRecommenderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class StopRecommenderResponse(TypedDict, closed=True):
    recommender_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recommender you stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopRecommenderResponse) -> dict:
    out: dict = {}
    if "recommender_arn" in value:
        out["recommenderArn"] = value["recommender_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopRecommenderResponse:
    out: StopRecommenderResponse = {}  # type: ignore[typeddict-item]
    if "recommenderArn" in data:
        out["recommender_arn"] = data["recommenderArn"]
    return out
