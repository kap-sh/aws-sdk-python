"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmValidationProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_validation_profile

AlgorithmValidationProfiles: TypeAlias = list[
    "aws_sdk_sagemaker.types.algorithm_validation_profile.AlgorithmValidationProfile"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmValidationProfiles) -> list:
    import aws_sdk_sagemaker.types.algorithm_validation_profile

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.algorithm_validation_profile.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AlgorithmValidationProfiles:
    import aws_sdk_sagemaker.types.algorithm_validation_profile

    out: AlgorithmValidationProfiles = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.algorithm_validation_profile.deserialize_aws_json_1_1(
                item
            )
        )
    return out
