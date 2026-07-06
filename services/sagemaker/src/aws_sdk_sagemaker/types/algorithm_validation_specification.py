"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmValidationSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_validation_profiles
    import aws_sdk_sagemaker.types.role_arn


class AlgorithmValidationSpecification(TypedDict, closed=True):
    validation_role: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The IAM roles that SageMaker uses to run the training jobs.</p>"""
    validation_profiles: NotRequired[
        "aws_sdk_sagemaker.types.algorithm_validation_profiles.AlgorithmValidationProfiles"
    ]
    """<p>An array of <code>AlgorithmValidationProfile</code> objects, each of which specifies a training job and batch transform job that SageMaker runs to validate your algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmValidationSpecification) -> dict:
    out: dict = {}
    if "validation_role" in value:
        out["ValidationRole"] = value["validation_role"]
    if "validation_profiles" in value:
        import aws_sdk_sagemaker.types.algorithm_validation_profiles

        out["ValidationProfiles"] = (
            aws_sdk_sagemaker.types.algorithm_validation_profiles.serialize_aws_json_1_1(
                value["validation_profiles"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlgorithmValidationSpecification:
    out: AlgorithmValidationSpecification = {}  # type: ignore[typeddict-item]
    if "ValidationRole" in data:
        out["validation_role"] = data["ValidationRole"]
    if "ValidationProfiles" in data:
        import aws_sdk_sagemaker.types.algorithm_validation_profiles

        out["validation_profiles"] = (
            aws_sdk_sagemaker.types.algorithm_validation_profiles.deserialize_aws_json_1_1(
                data["ValidationProfiles"]
            )
        )
    return out
