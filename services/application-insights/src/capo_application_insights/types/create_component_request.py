"""Generated from Smithy shape ``com.amazonaws.applicationinsights#CreateComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_insights.types.custom_component_name
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.resource_list


class CreateComponentRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: (
        "capo_application_insights.types.custom_component_name.CustomComponentName"
    )
    """<p>The name of the component.</p>"""
    resource_list: "capo_application_insights.types.resource_list.ResourceList"
    """<p>The list of resource ARNs that belong to the component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateComponentRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    import capo_application_insights.types.resource_list

    out["ResourceList"] = (
        capo_application_insights.types.resource_list.serialize_aws_json_1_1(
            value["resource_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateComponentRequest:
    out: CreateComponentRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError(
            "CreateComponentRequest.resource_group_name required"
        )
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    else:
        raise DeserializationError("CreateComponentRequest.component_name required")
    if "ResourceList" in data:
        import capo_application_insights.types.resource_list

        out["resource_list"] = (
            capo_application_insights.types.resource_list.deserialize_aws_json_1_1(
                data["ResourceList"]
            )
        )
    else:
        raise DeserializationError("CreateComponentRequest.resource_list required")
    return out
