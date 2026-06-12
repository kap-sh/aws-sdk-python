"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateRecommenderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.recommender_config


class UpdateRecommenderRequest(TypedDict):
    recommender_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recommender to modify.</p>"""
    recommender_config: "aws_sdk_personalize.types.recommender_config.RecommenderConfig"
    """<p>The configuration details of the recommender.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRecommenderRequest) -> dict:
    out: dict = {}
    out["recommenderArn"] = value["recommender_arn"]
    import aws_sdk_personalize.types.recommender_config

    out["recommenderConfig"] = (
        aws_sdk_personalize.types.recommender_config.serialize_aws_json_1_1(
            value["recommender_config"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRecommenderRequest:
    out: UpdateRecommenderRequest = {}  # type: ignore[typeddict-item]
    if "recommenderArn" in data:
        out["recommender_arn"] = data["recommenderArn"]
    else:
        raise DeserializationError("UpdateRecommenderRequest.recommender_arn required")
    if "recommenderConfig" in data:
        import aws_sdk_personalize.types.recommender_config

        out["recommender_config"] = (
            aws_sdk_personalize.types.recommender_config.deserialize_aws_json_1_1(
                data["recommenderConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRecommenderRequest.recommender_config required"
        )
    return out
