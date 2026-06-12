"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateAppImageConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_image_config_arn


class UpdateAppImageConfigResponse(TypedDict):
    app_image_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.app_image_config_arn.AppImageConfigArn"
    ]
    """<p>The ARN for the AppImageConfig.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAppImageConfigResponse) -> dict:
    out: dict = {}
    if "app_image_config_arn" in value:
        out["AppImageConfigArn"] = value["app_image_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAppImageConfigResponse:
    out: UpdateAppImageConfigResponse = {}  # type: ignore[typeddict-item]
    if "AppImageConfigArn" in data:
        out["app_image_config_arn"] = data["AppImageConfigArn"]
    return out
