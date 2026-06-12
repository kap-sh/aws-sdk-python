"""Generated from Smithy shape ``com.amazonaws.sagemaker#DockerSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_status
    import aws_sdk_sagemaker.types.vpc_only_trusted_accounts


class DockerSettings(TypedDict):
    enable_docker_access: NotRequired[
        "aws_sdk_sagemaker.types.feature_status.FeatureStatus"
    ]
    """<p>Indicates whether the domain can access Docker.</p>"""
    vpc_only_trusted_accounts: NotRequired[
        "aws_sdk_sagemaker.types.vpc_only_trusted_accounts.VpcOnlyTrustedAccounts"
    ]
    """<p>The list of Amazon Web Services accounts that are trusted when the domain is created in VPC-only mode.</p>"""
    rootless_docker: NotRequired["aws_sdk_sagemaker.types.feature_status.FeatureStatus"]
    """<p>Indicates whether to use rootless Docker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DockerSettings) -> dict:
    out: dict = {}
    if "enable_docker_access" in value:
        import aws_sdk_sagemaker.types.feature_status

        out["EnableDockerAccess"] = (
            aws_sdk_sagemaker.types.feature_status.serialize_aws_json_1_1(
                value["enable_docker_access"]
            )
        )
    if "vpc_only_trusted_accounts" in value:
        import aws_sdk_sagemaker.types.vpc_only_trusted_accounts

        out["VpcOnlyTrustedAccounts"] = (
            aws_sdk_sagemaker.types.vpc_only_trusted_accounts.serialize_aws_json_1_1(
                value["vpc_only_trusted_accounts"]
            )
        )
    if "rootless_docker" in value:
        import aws_sdk_sagemaker.types.feature_status

        out["RootlessDocker"] = (
            aws_sdk_sagemaker.types.feature_status.serialize_aws_json_1_1(
                value["rootless_docker"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DockerSettings:
    out: DockerSettings = {}  # type: ignore[typeddict-item]
    if "EnableDockerAccess" in data:
        import aws_sdk_sagemaker.types.feature_status

        out["enable_docker_access"] = (
            aws_sdk_sagemaker.types.feature_status.deserialize_aws_json_1_1(
                data["EnableDockerAccess"]
            )
        )
    if "VpcOnlyTrustedAccounts" in data:
        import aws_sdk_sagemaker.types.vpc_only_trusted_accounts

        out["vpc_only_trusted_accounts"] = (
            aws_sdk_sagemaker.types.vpc_only_trusted_accounts.deserialize_aws_json_1_1(
                data["VpcOnlyTrustedAccounts"]
            )
        )
    if "RootlessDocker" in data:
        import aws_sdk_sagemaker.types.feature_status

        out["rootless_docker"] = (
            aws_sdk_sagemaker.types.feature_status.deserialize_aws_json_1_1(
                data["RootlessDocker"]
            )
        )
    return out
