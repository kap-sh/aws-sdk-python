"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.logical_resource_id
    import aws_sdk_resiliencehub.types.physical_resource_id
    import aws_sdk_resiliencehub.types.string255
    import aws_sdk_resiliencehub.types.string255_list


class GroupingResource(TypedDict, closed=True):
    resource_name: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Indicates the resource name.</p>"""
    resource_type: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Indicates the resource type.</p>"""
    physical_resource_id: (
        "aws_sdk_resiliencehub.types.physical_resource_id.PhysicalResourceId"
    )
    """<p>Indicates the physical identifier of the resource.</p>"""
    logical_resource_id: (
        "aws_sdk_resiliencehub.types.logical_resource_id.LogicalResourceId"
    )
    """<p>Indicates the logical identifier of the resource.</p>"""
    source_app_component_ids: "aws_sdk_resiliencehub.types.string255_list.String255List"
    """<p>Indicates the identifier of the source AppComponents in which the resources were previously grouped into.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupingResource) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    out["resourceType"] = value["resource_type"]
    import aws_sdk_resiliencehub.types.physical_resource_id

    out["physicalResourceId"] = (
        aws_sdk_resiliencehub.types.physical_resource_id.serialize_json(
            value["physical_resource_id"]
        )
    )
    import aws_sdk_resiliencehub.types.logical_resource_id

    out["logicalResourceId"] = (
        aws_sdk_resiliencehub.types.logical_resource_id.serialize_json(
            value["logical_resource_id"]
        )
    )
    import aws_sdk_resiliencehub.types.string255_list

    out["sourceAppComponentIds"] = (
        aws_sdk_resiliencehub.types.string255_list.serialize_json(
            value["source_app_component_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> GroupingResource:
    out: GroupingResource = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError("GroupingResource.resource_name required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("GroupingResource.resource_type required")
    if "physicalResourceId" in data:
        import aws_sdk_resiliencehub.types.physical_resource_id

        out["physical_resource_id"] = (
            aws_sdk_resiliencehub.types.physical_resource_id.deserialize_json(
                data["physicalResourceId"]
            )
        )
    else:
        raise DeserializationError("GroupingResource.physical_resource_id required")
    if "logicalResourceId" in data:
        import aws_sdk_resiliencehub.types.logical_resource_id

        out["logical_resource_id"] = (
            aws_sdk_resiliencehub.types.logical_resource_id.deserialize_json(
                data["logicalResourceId"]
            )
        )
    else:
        raise DeserializationError("GroupingResource.logical_resource_id required")
    if "sourceAppComponentIds" in data:
        import aws_sdk_resiliencehub.types.string255_list

        out["source_app_component_ids"] = (
            aws_sdk_resiliencehub.types.string255_list.deserialize_json(
                data["sourceAppComponentIds"]
            )
        )
    else:
        raise DeserializationError("GroupingResource.source_app_component_ids required")
    return out
