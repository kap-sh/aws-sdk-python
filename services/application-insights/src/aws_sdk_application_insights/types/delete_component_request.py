"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DeleteComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.custom_component_name
    import aws_sdk_application_insights.types.resource_group_name


class DeleteComponentRequest(TypedDict, closed=True):
    resource_group_name: (
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: (
        "aws_sdk_application_insights.types.custom_component_name.CustomComponentName"
    )
    """<p>The name of the component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteComponentRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteComponentRequest:
    out: DeleteComponentRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError(
            "DeleteComponentRequest.resource_group_name required"
        )
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    else:
        raise DeserializationError("DeleteComponentRequest.component_name required")
    return out
