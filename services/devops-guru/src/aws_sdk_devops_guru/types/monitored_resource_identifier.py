"""Generated from Smithy shape ``com.amazonaws.devopsguru#MonitoredResourceIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.monitored_resource_name
    import aws_sdk_devops_guru.types.resource_collection
    import aws_sdk_devops_guru.types.resource_permission
    import aws_sdk_devops_guru.types.resource_type
    import aws_sdk_devops_guru.types.timestamp


class MonitoredResourceIdentifier(TypedDict, closed=True):
    monitored_resource_name: NotRequired[
        "aws_sdk_devops_guru.types.monitored_resource_name.MonitoredResourceName"
    ]
    """<p> The name of the resource being monitored. </p>"""
    type: NotRequired["aws_sdk_devops_guru.types.resource_type.ResourceType"]
    """<p> The type of resource being monitored. </p>"""
    resource_permission: NotRequired[
        "aws_sdk_devops_guru.types.resource_permission.ResourcePermission"
    ]
    """<p> The permission status of a resource. </p>"""
    last_updated: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The time at which DevOps Guru last updated this resource. </p>"""
    resource_collection: NotRequired[
        "aws_sdk_devops_guru.types.resource_collection.ResourceCollection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MonitoredResourceIdentifier) -> dict:
    out: dict = {}
    if "monitored_resource_name" in value:
        out["MonitoredResourceName"] = value["monitored_resource_name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "resource_permission" in value:
        import aws_sdk_devops_guru.types.resource_permission

        out["ResourcePermission"] = (
            aws_sdk_devops_guru.types.resource_permission.serialize_json(
                value["resource_permission"]
            )
        )
    if "last_updated" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["LastUpdated"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["last_updated"]
        )
    if "resource_collection" in value:
        import aws_sdk_devops_guru.types.resource_collection

        out["ResourceCollection"] = (
            aws_sdk_devops_guru.types.resource_collection.serialize_json(
                value["resource_collection"]
            )
        )
    return out


def deserialize_json(data: dict) -> MonitoredResourceIdentifier:
    out: MonitoredResourceIdentifier = {}  # type: ignore[typeddict-item]
    if "MonitoredResourceName" in data:
        out["monitored_resource_name"] = data["MonitoredResourceName"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "ResourcePermission" in data:
        import aws_sdk_devops_guru.types.resource_permission

        out["resource_permission"] = (
            aws_sdk_devops_guru.types.resource_permission.deserialize_json(
                data["ResourcePermission"]
            )
        )
    if "LastUpdated" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["last_updated"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["LastUpdated"]
        )
    if "ResourceCollection" in data:
        import aws_sdk_devops_guru.types.resource_collection

        out["resource_collection"] = (
            aws_sdk_devops_guru.types.resource_collection.deserialize_json(
                data["ResourceCollection"]
            )
        )
    return out
