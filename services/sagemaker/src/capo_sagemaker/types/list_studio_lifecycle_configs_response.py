"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListStudioLifecycleConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.studio_lifecycle_configs_list


class ListStudioLifecycleConfigsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""
    studio_lifecycle_configs: NotRequired[
        "capo_sagemaker.types.studio_lifecycle_configs_list.StudioLifecycleConfigsList"
    ]
    """<p>A list of Lifecycle Configurations and their properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStudioLifecycleConfigsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "studio_lifecycle_configs" in value:
        import capo_sagemaker.types.studio_lifecycle_configs_list

        out["StudioLifecycleConfigs"] = (
            capo_sagemaker.types.studio_lifecycle_configs_list.serialize_aws_json_1_1(
                value["studio_lifecycle_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStudioLifecycleConfigsResponse:
    out: ListStudioLifecycleConfigsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "StudioLifecycleConfigs" in data:
        import capo_sagemaker.types.studio_lifecycle_configs_list

        out["studio_lifecycle_configs"] = (
            capo_sagemaker.types.studio_lifecycle_configs_list.deserialize_aws_json_1_1(
                data["StudioLifecycleConfigs"]
            )
        )
    return out
