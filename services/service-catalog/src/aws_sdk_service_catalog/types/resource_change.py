"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceChange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.change_action
    import aws_sdk_service_catalog.types.logical_resource_id
    import aws_sdk_service_catalog.types.physical_resource_id
    import aws_sdk_service_catalog.types.plan_resource_type
    import aws_sdk_service_catalog.types.replacement
    import aws_sdk_service_catalog.types.resource_change_details
    import aws_sdk_service_catalog.types.scope


class ResourceChange(TypedDict):
    action: NotRequired["aws_sdk_service_catalog.types.change_action.ChangeAction"]
    """<p>The change action.</p>"""
    logical_resource_id: NotRequired[
        "aws_sdk_service_catalog.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The ID of the resource, as defined in the CloudFormation template.</p>"""
    physical_resource_id: NotRequired[
        "aws_sdk_service_catalog.types.physical_resource_id.PhysicalResourceId"
    ]
    """<p>The ID of the resource, if it was already created.</p>"""
    resource_type: NotRequired[
        "aws_sdk_service_catalog.types.plan_resource_type.PlanResourceType"
    ]
    """<p>The type of resource.</p>"""
    replacement: NotRequired["aws_sdk_service_catalog.types.replacement.Replacement"]
    """<p>If the change type is <code>Modify</code>, indicates whether the existing resource is deleted and replaced with a new one.</p>"""
    scope: NotRequired["aws_sdk_service_catalog.types.scope.Scope"]
    """<p>The change scope.</p>"""
    details: NotRequired[
        "aws_sdk_service_catalog.types.resource_change_details.ResourceChangeDetails"
    ]
    """<p>Information about the resource changes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceChange) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_service_catalog.types.change_action

        out["Action"] = (
            aws_sdk_service_catalog.types.change_action.serialize_aws_json_1_1(
                value["action"]
            )
        )
    if "logical_resource_id" in value:
        out["LogicalResourceId"] = value["logical_resource_id"]
    if "physical_resource_id" in value:
        out["PhysicalResourceId"] = value["physical_resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "replacement" in value:
        import aws_sdk_service_catalog.types.replacement

        out["Replacement"] = (
            aws_sdk_service_catalog.types.replacement.serialize_aws_json_1_1(
                value["replacement"]
            )
        )
    if "scope" in value:
        import aws_sdk_service_catalog.types.scope

        out["Scope"] = aws_sdk_service_catalog.types.scope.serialize_aws_json_1_1(
            value["scope"]
        )
    if "details" in value:
        import aws_sdk_service_catalog.types.resource_change_details

        out["Details"] = (
            aws_sdk_service_catalog.types.resource_change_details.serialize_aws_json_1_1(
                value["details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceChange:
    out: ResourceChange = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_service_catalog.types.change_action

        out["action"] = (
            aws_sdk_service_catalog.types.change_action.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    if "LogicalResourceId" in data:
        out["logical_resource_id"] = data["LogicalResourceId"]
    if "PhysicalResourceId" in data:
        out["physical_resource_id"] = data["PhysicalResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "Replacement" in data:
        import aws_sdk_service_catalog.types.replacement

        out["replacement"] = (
            aws_sdk_service_catalog.types.replacement.deserialize_aws_json_1_1(
                data["Replacement"]
            )
        )
    if "Scope" in data:
        import aws_sdk_service_catalog.types.scope

        out["scope"] = aws_sdk_service_catalog.types.scope.deserialize_aws_json_1_1(
            data["Scope"]
        )
    if "Details" in data:
        import aws_sdk_service_catalog.types.resource_change_details

        out["details"] = (
            aws_sdk_service_catalog.types.resource_change_details.deserialize_aws_json_1_1(
                data["Details"]
            )
        )
    return out
