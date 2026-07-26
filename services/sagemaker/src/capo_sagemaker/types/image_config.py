"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.repository_access_mode
    import capo_sagemaker.types.repository_auth_config


class ImageConfig(TypedDict, closed=True):
    repository_access_mode: NotRequired[
        "capo_sagemaker.types.repository_access_mode.RepositoryAccessMode"
    ]
    """<p>Set this to one of the following values:</p> <ul> <li> <p> <code>Platform</code> - The model image is hosted in Amazon ECR.</p> </li> <li> <p> <code>Vpc</code> - The model image is hosted in a private Docker registry in your VPC.</p> </li> </ul>"""
    repository_auth_config: NotRequired[
        "capo_sagemaker.types.repository_auth_config.RepositoryAuthConfig"
    ]
    """<p>(Optional) Specifies an authentication configuration for the private docker registry where your model image is hosted. Specify a value for this property only if you specified <code>Vpc</code> as the value for the <code>RepositoryAccessMode</code> field, and the private Docker registry where the model image is hosted requires authentication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageConfig) -> dict:
    out: dict = {}
    if "repository_access_mode" in value:
        import capo_sagemaker.types.repository_access_mode

        out["RepositoryAccessMode"] = (
            capo_sagemaker.types.repository_access_mode.serialize_aws_json_1_1(
                value["repository_access_mode"]
            )
        )
    if "repository_auth_config" in value:
        import capo_sagemaker.types.repository_auth_config

        out["RepositoryAuthConfig"] = (
            capo_sagemaker.types.repository_auth_config.serialize_aws_json_1_1(
                value["repository_auth_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageConfig:
    out: ImageConfig = {}  # type: ignore[typeddict-item]
    if "RepositoryAccessMode" in data:
        import capo_sagemaker.types.repository_access_mode

        out["repository_access_mode"] = (
            capo_sagemaker.types.repository_access_mode.deserialize_aws_json_1_1(
                data["RepositoryAccessMode"]
            )
        )
    if "RepositoryAuthConfig" in data:
        import capo_sagemaker.types.repository_auth_config

        out["repository_auth_config"] = (
            capo_sagemaker.types.repository_auth_config.deserialize_aws_json_1_1(
                data["RepositoryAuthConfig"]
            )
        )
    return out
