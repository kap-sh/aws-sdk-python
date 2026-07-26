"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageValidationProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.model_package_validation_profile

ModelPackageValidationProfiles: TypeAlias = list[
    "capo_sagemaker.types.model_package_validation_profile.ModelPackageValidationProfile"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageValidationProfiles) -> list:
    import capo_sagemaker.types.model_package_validation_profile

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.model_package_validation_profile.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelPackageValidationProfiles:
    import capo_sagemaker.types.model_package_validation_profile

    out: ModelPackageValidationProfiles = []
    for item in data:
        out.append(
            capo_sagemaker.types.model_package_validation_profile.deserialize_aws_json_1_1(
                item
            )
        )
    return out
