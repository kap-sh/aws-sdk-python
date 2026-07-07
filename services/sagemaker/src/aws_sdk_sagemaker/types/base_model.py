"""Generated from Smithy shape ``com.amazonaws.sagemaker#BaseModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_content_name
    import aws_sdk_sagemaker.types.hub_content_version
    import aws_sdk_sagemaker.types.recipe_name


class BaseModel(TypedDict, closed=True):
    hub_content_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p> The hub content name of the base model. </p>"""
    hub_content_version: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p> The hub content version of the base model. </p>"""
    recipe_name: NotRequired["aws_sdk_sagemaker.types.recipe_name.RecipeName"]
    """<p> The recipe name of the base model. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BaseModel) -> dict:
    out: dict = {}
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "hub_content_version" in value:
        out["HubContentVersion"] = value["hub_content_version"]
    if "recipe_name" in value:
        out["RecipeName"] = value["recipe_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BaseModel:
    out: BaseModel = {}  # type: ignore[typeddict-item]
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "HubContentVersion" in data:
        out["hub_content_version"] = data["HubContentVersion"]
    if "RecipeName" in data:
        out["recipe_name"] = data["RecipeName"]
    return out
