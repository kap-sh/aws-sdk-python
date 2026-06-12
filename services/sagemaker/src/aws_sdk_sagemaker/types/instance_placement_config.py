"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstancePlacementConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.placement_specifications


class InstancePlacementConfig(TypedDict):
    enable_multiple_jobs: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>If set to true, allows multiple jobs to share the same UltraServer instances. If set to false, ensures this job's instances are placed on an UltraServer exclusively, with no other jobs sharing the same UltraServer. Default is false.</p>"""
    placement_specifications: NotRequired[
        "aws_sdk_sagemaker.types.placement_specifications.PlacementSpecifications"
    ]
    """<p>A list of specifications for how instances should be placed on specific UltraServers. Maximum of 10 items is supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePlacementConfig) -> dict:
    out: dict = {}
    if "enable_multiple_jobs" in value:
        out["EnableMultipleJobs"] = value["enable_multiple_jobs"]
    if "placement_specifications" in value:
        import aws_sdk_sagemaker.types.placement_specifications

        out["PlacementSpecifications"] = (
            aws_sdk_sagemaker.types.placement_specifications.serialize_aws_json_1_1(
                value["placement_specifications"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstancePlacementConfig:
    out: InstancePlacementConfig = {}  # type: ignore[typeddict-item]
    if "EnableMultipleJobs" in data:
        out["enable_multiple_jobs"] = data["EnableMultipleJobs"]
    if "PlacementSpecifications" in data:
        import aws_sdk_sagemaker.types.placement_specifications

        out["placement_specifications"] = (
            aws_sdk_sagemaker.types.placement_specifications.deserialize_aws_json_1_1(
                data["PlacementSpecifications"]
            )
        )
    return out
