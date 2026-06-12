"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateRecommenderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class UpdateRecommenderResponse(TypedDict):
    recommender_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
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
