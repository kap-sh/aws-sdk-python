"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteAppImageConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_image_config_name


class DeleteAppImageConfigRequest(TypedDict, closed=True):
    app_image_config_name: NotRequired[
        "capo_sagemaker.types.app_image_config_name.AppImageConfigName"
    ]
    """<p>The name of the AppImageConfig to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAppImageConfigRequest) -> dict:
    out: dict = {}
    if "app_image_config_name" in value:
        out["AppImageConfigName"] = value["app_image_config_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAppImageConfigRequest:
    out: DeleteAppImageConfigRequest = {}  # type: ignore[typeddict-item]
    if "AppImageConfigName" in data:
        out["app_image_config_name"] = data["AppImageConfigName"]
    return out
