"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListMonitoredResourcesFilters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.resource_permission
    import aws_sdk_devops_guru.types.resource_type_filters


class ListMonitoredResourcesFilters(TypedDict):
    resource_permission: (
        "aws_sdk_devops_guru.types.resource_permission.ResourcePermission"
    )
    """<p> The permission status of a resource. </p>"""
    resource_type_filters: (
        "aws_sdk_devops_guru.types.resource_type_filters.ResourceTypeFilters"
    )
    """<p> The type of resource that you wish to retrieve, such as log groups. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitoredResourcesFilters) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.resource_permission

    out["ResourcePermission"] = (
        aws_sdk_devops_guru.types.resource_permission.serialize_json(
            value["resource_permission"]
        )
    )
    import aws_sdk_devops_guru.types.resource_type_filters

    out["ResourceTypeFilters"] = (
        aws_sdk_devops_guru.types.resource_type_filters.serialize_json(
            value["resource_type_filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMonitoredResourcesFilters:
    out: ListMonitoredResourcesFilters = {}  # type: ignore[typeddict-item]
    if "ResourcePermission" in data:
        import aws_sdk_devops_guru.types.resource_permission

        out["resource_permission"] = (
            aws_sdk_devops_guru.types.resource_permission.deserialize_json(
                data["ResourcePermission"]
            )
        )
    else:
        raise DeserializationError(
            "ListMonitoredResourcesFilters.resource_permission required"
        )
    if "ResourceTypeFilters" in data:
        import aws_sdk_devops_guru.types.resource_type_filters

        out["resource_type_filters"] = (
            aws_sdk_devops_guru.types.resource_type_filters.deserialize_json(
                data["ResourceTypeFilters"]
            )
        )
    else:
        raise DeserializationError(
            "ListMonitoredResourcesFilters.resource_type_filters required"
        )
    return out
