"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeFeatureTransformationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.feature_transformation


class DescribeFeatureTransformationResponse(TypedDict):
    feature_transformation: NotRequired[
        "aws_sdk_personalize.types.feature_transformation.FeatureTransformation"
    ]
    """<p>A listing of the FeatureTransformation properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeatureTransformationResponse) -> dict:
    out: dict = {}
    if "feature_transformation" in value:
        import aws_sdk_personalize.types.feature_transformation

        out["featureTransformation"] = (
            aws_sdk_personalize.types.feature_transformation.serialize_aws_json_1_1(
                value["feature_transformation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeatureTransformationResponse:
    out: DescribeFeatureTransformationResponse = {}  # type: ignore[typeddict-item]
    if "featureTransformation" in data:
        import aws_sdk_personalize.types.feature_transformation

        out["feature_transformation"] = (
            aws_sdk_personalize.types.feature_transformation.deserialize_aws_json_1_1(
                data["featureTransformation"]
            )
        )
    return out
