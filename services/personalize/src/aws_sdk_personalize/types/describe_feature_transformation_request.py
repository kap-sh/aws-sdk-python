"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeFeatureTransformationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeFeatureTransformationRequest(TypedDict):
    feature_transformation_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the feature transformation to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeatureTransformationRequest) -> dict:
    out: dict = {}
    out["featureTransformationArn"] = value["feature_transformation_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeatureTransformationRequest:
    out: DescribeFeatureTransformationRequest = {}  # type: ignore[typeddict-item]
    if "featureTransformationArn" in data:
        out["feature_transformation_arn"] = data["featureTransformationArn"]
    else:
        raise DeserializationError(
            "DescribeFeatureTransformationRequest.feature_transformation_arn required"
        )
    return out
