"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAppImageConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_image_config_list
    import capo_sagemaker.types.next_token


class ListAppImageConfigsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of AppImageConfigs, if there are any.</p>"""
    app_image_configs: NotRequired[
        "capo_sagemaker.types.app_image_config_list.AppImageConfigList"
    ]
    """<p>A list of AppImageConfigs and their properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAppImageConfigsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "app_image_configs" in value:
        import capo_sagemaker.types.app_image_config_list

        out["AppImageConfigs"] = (
            capo_sagemaker.types.app_image_config_list.serialize_aws_json_1_1(
                value["app_image_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAppImageConfigsResponse:
    out: ListAppImageConfigsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AppImageConfigs" in data:
        import capo_sagemaker.types.app_image_config_list

        out["app_image_configs"] = (
            capo_sagemaker.types.app_image_config_list.deserialize_aws_json_1_1(
                data["AppImageConfigs"]
            )
        )
    return out
