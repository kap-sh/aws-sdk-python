"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterRestrictedInstanceGroupsConfigOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_shared_environment_config_details


class ClusterRestrictedInstanceGroupsConfigOutput(TypedDict):
    shared_environment_config: NotRequired[
        "aws_sdk_sagemaker.types.cluster_shared_environment_config_details.ClusterSharedEnvironmentConfigDetails"
    ]
    """<p>The shared environment configuration details for the restricted instance groups (RIG).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterRestrictedInstanceGroupsConfigOutput) -> dict:
    out: dict = {}
    if "shared_environment_config" in value:
        import aws_sdk_sagemaker.types.cluster_shared_environment_config_details

        out["SharedEnvironmentConfig"] = (
            aws_sdk_sagemaker.types.cluster_shared_environment_config_details.serialize_aws_json_1_1(
                value["shared_environment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterRestrictedInstanceGroupsConfigOutput:
    out: ClusterRestrictedInstanceGroupsConfigOutput = {}  # type: ignore[typeddict-item]
    if "SharedEnvironmentConfig" in data:
        import aws_sdk_sagemaker.types.cluster_shared_environment_config_details

        out["shared_environment_config"] = (
            aws_sdk_sagemaker.types.cluster_shared_environment_config_details.deserialize_aws_json_1_1(
                data["SharedEnvironmentConfig"]
            )
        )
    return out
