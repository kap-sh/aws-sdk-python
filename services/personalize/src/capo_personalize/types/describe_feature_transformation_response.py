"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeFeatureTransformationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.feature_transformation


class DescribeFeatureTransformationResponse(TypedDict, closed=True):
    feature_transformation: NotRequired[
        "capo_personalize.types.feature_transformation.FeatureTransformation"
    ]
    """<p>A listing of the FeatureTransformation properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeatureTransformationResponse) -> dict:
    out: dict = {}
    if "feature_transformation" in value:
        import capo_personalize.types.feature_transformation

        out["featureTransformation"] = (
            capo_personalize.types.feature_transformation.serialize_aws_json_1_1(
                value["feature_transformation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeatureTransformationResponse:
    out: DescribeFeatureTransformationResponse = {}  # type: ignore[typeddict-item]
    if "featureTransformation" in data:
        import capo_personalize.types.feature_transformation

        out["feature_transformation"] = (
            capo_personalize.types.feature_transformation.deserialize_aws_json_1_1(
                data["featureTransformation"]
            )
        )
    return out
