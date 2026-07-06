"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingRepositoryAuthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_repository_credentials_provider_arn


class TrainingRepositoryAuthConfig(TypedDict, closed=True):
    training_repository_credentials_provider_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_repository_credentials_provider_arn.TrainingRepositoryCredentialsProviderArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services Lambda function used to give SageMaker access credentials to your private Docker registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingRepositoryAuthConfig) -> dict:
    out: dict = {}
    if "training_repository_credentials_provider_arn" in value:
        out["TrainingRepositoryCredentialsProviderArn"] = value[
            "training_repository_credentials_provider_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingRepositoryAuthConfig:
    out: TrainingRepositoryAuthConfig = {}  # type: ignore[typeddict-item]
    if "TrainingRepositoryCredentialsProviderArn" in data:
        out["training_repository_credentials_provider_arn"] = data[
            "TrainingRepositoryCredentialsProviderArn"
        ]
    return out
