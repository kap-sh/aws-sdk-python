"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAppImageConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_image_config_list
    import aws_sdk_sagemaker.types.next_token


class ListAppImageConfigsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of AppImageConfigs, if there are any.</p>"""
    app_image_configs: NotRequired[
        "aws_sdk_sagemaker.types.app_image_config_list.AppImageConfigList"
    ]
    """<p>A list of AppImageConfigs and their properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAppImageConfigsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "app_image_configs" in value:
        import aws_sdk_sagemaker.types.app_image_config_list

        out["AppImageConfigs"] = (
            aws_sdk_sagemaker.types.app_image_config_list.serialize_aws_json_1_1(
                value["app_image_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAppImageConfigsResponse:
    out: ListAppImageConfigsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AppImageConfigs" in data:
        import aws_sdk_sagemaker.types.app_image_config_list

        out["app_image_configs"] = (
            aws_sdk_sagemaker.types.app_image_config_list.deserialize_aws_json_1_1(
                data["AppImageConfigs"]
            )
        )
    return out
