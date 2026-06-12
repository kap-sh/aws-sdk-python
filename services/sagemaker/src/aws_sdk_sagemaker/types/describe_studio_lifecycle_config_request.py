"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeStudioLifecycleConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.studio_lifecycle_config_name


class DescribeStudioLifecycleConfigRequest(TypedDict):
    studio_lifecycle_config_name: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_name.StudioLifecycleConfigName"
    ]
    """<p>The name of the Amazon SageMaker AI Studio Lifecycle Configuration to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStudioLifecycleConfigRequest) -> dict:
    out: dict = {}
    if "studio_lifecycle_config_name" in value:
        out["StudioLifecycleConfigName"] = value["studio_lifecycle_config_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStudioLifecycleConfigRequest:
    out: DescribeStudioLifecycleConfigRequest = {}  # type: ignore[typeddict-item]
    if "StudioLifecycleConfigName" in data:
        out["studio_lifecycle_config_name"] = data["StudioLifecycleConfigName"]
    return out
