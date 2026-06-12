"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateStudioLifecycleConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.studio_lifecycle_config_arn


class CreateStudioLifecycleConfigResponse(TypedDict):
    studio_lifecycle_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_arn.StudioLifecycleConfigArn"
    ]
    """<p>The ARN of your created Lifecycle Configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStudioLifecycleConfigResponse) -> dict:
    out: dict = {}
    if "studio_lifecycle_config_arn" in value:
        out["StudioLifecycleConfigArn"] = value["studio_lifecycle_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStudioLifecycleConfigResponse:
    out: CreateStudioLifecycleConfigResponse = {}  # type: ignore[typeddict-item]
    if "StudioLifecycleConfigArn" in data:
        out["studio_lifecycle_config_arn"] = data["StudioLifecycleConfigArn"]
    return out
