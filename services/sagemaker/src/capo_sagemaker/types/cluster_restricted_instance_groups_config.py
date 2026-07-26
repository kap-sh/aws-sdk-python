"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterRestrictedInstanceGroupsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_shared_environment_config


class ClusterRestrictedInstanceGroupsConfig(TypedDict, closed=True):
    shared_environment_config: NotRequired[
        "capo_sagemaker.types.cluster_shared_environment_config.ClusterSharedEnvironmentConfig"
    ]
    """<p>The shared environment configuration for the restricted instance groups (RIG).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterRestrictedInstanceGroupsConfig) -> dict:
    out: dict = {}
    if "shared_environment_config" in value:
        import capo_sagemaker.types.cluster_shared_environment_config

        out["SharedEnvironmentConfig"] = (
            capo_sagemaker.types.cluster_shared_environment_config.serialize_aws_json_1_1(
                value["shared_environment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterRestrictedInstanceGroupsConfig:
    out: ClusterRestrictedInstanceGroupsConfig = {}  # type: ignore[typeddict-item]
    if "SharedEnvironmentConfig" in data:
        import capo_sagemaker.types.cluster_shared_environment_config

        out["shared_environment_config"] = (
            capo_sagemaker.types.cluster_shared_environment_config.deserialize_aws_json_1_1(
                data["SharedEnvironmentConfig"]
            )
        )
    return out
