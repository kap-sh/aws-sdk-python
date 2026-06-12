"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateComponentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.custom_component_name
    import aws_sdk_application_insights.types.resource_group_name
    import aws_sdk_application_insights.types.resource_list


class UpdateComponentRequest(TypedDict):
    resource_group_name: (
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: (
        "aws_sdk_application_insights.types.custom_component_name.CustomComponentName"
    )
    """<p>The name of the component.</p>"""
    new_component_name: NotRequired[
        "aws_sdk_application_insights.types.custom_component_name.CustomComponentName"
    ]
    """<p>The new name of the component.</p>"""
    resource_list: NotRequired[
        "aws_sdk_application_insights.types.resource_list.ResourceList"
    ]
    """<p>The list of resource ARNs that belong to the component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateComponentRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    if "new_component_name" in value:
        out["NewComponentName"] = value["new_component_name"]
    if "resource_list" in value:
        import aws_sdk_application_insights.types.resource_list

        out["ResourceList"] = (
            aws_sdk_application_insights.types.resource_list.serialize_aws_json_1_1(
                value["resource_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateComponentRequest:
    out: UpdateComponentRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError(
            "UpdateComponentRequest.resource_group_name required"
        )
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    else:
        raise DeserializationError("UpdateComponentRequest.component_name required")
    if "NewComponentName" in data:
        out["new_component_name"] = data["NewComponentName"]
    if "ResourceList" in data:
        import aws_sdk_application_insights.types.resource_list

        out["resource_list"] = (
            aws_sdk_application_insights.types.resource_list.deserialize_aws_json_1_1(
                data["ResourceList"]
            )
        )
    return out
