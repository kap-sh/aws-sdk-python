"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingImageConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_repository_access_mode
    import aws_sdk_sagemaker.types.training_repository_auth_config


class TrainingImageConfig(TypedDict):
    training_repository_access_mode: NotRequired[
        "aws_sdk_sagemaker.types.training_repository_access_mode.TrainingRepositoryAccessMode"
    ]
    """<p>The method that your training job will use to gain access to the images in your private Docker registry. For access to an image in a private Docker registry, set to <code>Vpc</code>.</p>"""
    training_repository_auth_config: NotRequired[
        "aws_sdk_sagemaker.types.training_repository_auth_config.TrainingRepositoryAuthConfig"
    ]
    """<p>An object containing authentication information for a private Docker registry containing your training images.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingImageConfig) -> dict:
    out: dict = {}
    if "training_repository_access_mode" in value:
        import aws_sdk_sagemaker.types.training_repository_access_mode

        out["TrainingRepositoryAccessMode"] = (
            aws_sdk_sagemaker.types.training_repository_access_mode.serialize_aws_json_1_1(
                value["training_repository_access_mode"]
            )
        )
    if "training_repository_auth_config" in value:
        import aws_sdk_sagemaker.types.training_repository_auth_config

        out["TrainingRepositoryAuthConfig"] = (
            aws_sdk_sagemaker.types.training_repository_auth_config.serialize_aws_json_1_1(
                value["training_repository_auth_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingImageConfig:
    out: TrainingImageConfig = {}  # type: ignore[typeddict-item]
    if "TrainingRepositoryAccessMode" in data:
        import aws_sdk_sagemaker.types.training_repository_access_mode

        out["training_repository_access_mode"] = (
            aws_sdk_sagemaker.types.training_repository_access_mode.deserialize_aws_json_1_1(
                data["TrainingRepositoryAccessMode"]
            )
        )
    if "TrainingRepositoryAuthConfig" in data:
        import aws_sdk_sagemaker.types.training_repository_auth_config

        out["training_repository_auth_config"] = (
            aws_sdk_sagemaker.types.training_repository_auth_config.deserialize_aws_json_1_1(
                data["TrainingRepositoryAuthConfig"]
            )
        )
    return out
