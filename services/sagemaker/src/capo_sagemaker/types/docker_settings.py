"""Generated from Smithy shape ``com.amazonaws.sagemaker#DockerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_status
    import capo_sagemaker.types.vpc_only_trusted_accounts


class DockerSettings(TypedDict, closed=True):
    enable_docker_access: NotRequired[
        "capo_sagemaker.types.feature_status.FeatureStatus"
    ]
    """<p>Indicates whether the domain can access Docker.</p>"""
    vpc_only_trusted_accounts: NotRequired[
        "capo_sagemaker.types.vpc_only_trusted_accounts.VpcOnlyTrustedAccounts"
    ]
    """<p>The list of Amazon Web Services accounts that are trusted when the domain is created in VPC-only mode.</p>"""
    rootless_docker: NotRequired["capo_sagemaker.types.feature_status.FeatureStatus"]
    """<p>Indicates whether to use rootless Docker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DockerSettings) -> dict:
    out: dict = {}
    if "enable_docker_access" in value:
        import capo_sagemaker.types.feature_status

        out["EnableDockerAccess"] = (
            capo_sagemaker.types.feature_status.serialize_aws_json_1_1(
                value["enable_docker_access"]
            )
        )
    if "vpc_only_trusted_accounts" in value:
        import capo_sagemaker.types.vpc_only_trusted_accounts

        out["VpcOnlyTrustedAccounts"] = (
            capo_sagemaker.types.vpc_only_trusted_accounts.serialize_aws_json_1_1(
                value["vpc_only_trusted_accounts"]
            )
        )
    if "rootless_docker" in value:
        import capo_sagemaker.types.feature_status

        out["RootlessDocker"] = (
            capo_sagemaker.types.feature_status.serialize_aws_json_1_1(
                value["rootless_docker"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DockerSettings:
    out: DockerSettings = {}  # type: ignore[typeddict-item]
    if "EnableDockerAccess" in data:
        import capo_sagemaker.types.feature_status

        out["enable_docker_access"] = (
            capo_sagemaker.types.feature_status.deserialize_aws_json_1_1(
                data["EnableDockerAccess"]
            )
        )
    if "VpcOnlyTrustedAccounts" in data:
        import capo_sagemaker.types.vpc_only_trusted_accounts

        out["vpc_only_trusted_accounts"] = (
            capo_sagemaker.types.vpc_only_trusted_accounts.deserialize_aws_json_1_1(
                data["VpcOnlyTrustedAccounts"]
            )
        )
    if "RootlessDocker" in data:
        import capo_sagemaker.types.feature_status

        out["rootless_docker"] = (
            capo_sagemaker.types.feature_status.deserialize_aws_json_1_1(
                data["RootlessDocker"]
            )
        )
    return out
