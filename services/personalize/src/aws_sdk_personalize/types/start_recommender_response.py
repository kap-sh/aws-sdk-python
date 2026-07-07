"""Generated from Smithy shape ``com.amazonaws.personalize#StartRecommenderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class StartRecommenderResponse(TypedDict, closed=True):
    recommender_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recommender you started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRecommenderResponse) -> dict:
    out: dict = {}
    if "recommender_arn" in value:
        out["recommenderArn"] = value["recommender_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRecommenderResponse:
    out: StartRecommenderResponse = {}  # type: ignore[typeddict-item]
    if "recommenderArn" in data:
        out["recommender_arn"] = data["recommenderArn"]
    return out
