"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageValidationSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_package_validation_profiles
    import aws_sdk_sagemaker.types.role_arn


class ModelPackageValidationSpecification(TypedDict):
    validation_role: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The IAM roles to be used for the validation of the model package.</p>"""
    validation_profiles: NotRequired[
        "aws_sdk_sagemaker.types.model_package_validation_profiles.ModelPackageValidationProfiles"
    ]
    """<p>An array of <code>ModelPackageValidationProfile</code> objects, each of which specifies a batch transform job that SageMaker runs to validate your model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageValidationSpecification) -> dict:
    out: dict = {}
    if "validation_role" in value:
        out["ValidationRole"] = value["validation_role"]
    if "validation_profiles" in value:
        import aws_sdk_sagemaker.types.model_package_validation_profiles

        out["ValidationProfiles"] = (
            aws_sdk_sagemaker.types.model_package_validation_profiles.serialize_aws_json_1_1(
                value["validation_profiles"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageValidationSpecification:
    out: ModelPackageValidationSpecification = {}  # type: ignore[typeddict-item]
    if "ValidationRole" in data:
        out["validation_role"] = data["ValidationRole"]
    if "ValidationProfiles" in data:
        import aws_sdk_sagemaker.types.model_package_validation_profiles

        out["validation_profiles"] = (
            aws_sdk_sagemaker.types.model_package_validation_profiles.deserialize_aws_json_1_1(
                data["ValidationProfiles"]
            )
        )
    return out
