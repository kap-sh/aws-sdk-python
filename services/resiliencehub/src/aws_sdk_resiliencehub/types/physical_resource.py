"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PhysicalResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.additional_info_map
    import aws_sdk_resiliencehub.types.app_component_list
    import aws_sdk_resiliencehub.types.boolean_optional
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.logical_resource_id
    import aws_sdk_resiliencehub.types.physical_resource_id
    import aws_sdk_resiliencehub.types.resource_source_type
    import aws_sdk_resiliencehub.types.string255


class PhysicalResource(TypedDict):
    resource_name: NotRequired["aws_sdk_resiliencehub.types.entity_name.EntityName"]
    """<p>The name of the resource.</p>"""
    logical_resource_id: (
        "aws_sdk_resiliencehub.types.logical_resource_id.LogicalResourceId"
    )
    """<p>Logical identifier of the resource.</p>"""
    physical_resource_id: (
        "aws_sdk_resiliencehub.types.physical_resource_id.PhysicalResourceId"
    )
    """<p>Identifier of the physical resource.</p>"""
    resource_type: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Type of resource.</p>"""
    app_components: NotRequired[
        "aws_sdk_resiliencehub.types.app_component_list.AppComponentList"
    ]
    """<p>The application components that belong to this resource.</p>"""
    additional_info: NotRequired[
        "aws_sdk_resiliencehub.types.additional_info_map.AdditionalInfoMap"
    ]
    r"""<p>Additional configuration parameters for an Resilience Hub application. If you want to implement <code>additionalInfo</code> through the Resilience Hub console rather than using an API call, see <a href=\"https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html\">Configure the application configuration parameters</a>.</p> <note> <p>Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.</p> <p>Key: <code>\"failover-regions\"</code> </p> <p>Value: <code>\"[{\"region\":\"&lt;REGION&gt;\", \"accounts\":[{\"id\":\"&lt;ACCOUNT_ID&gt;\"}]}]\"</code> </p> </note>"""
    excluded: NotRequired[
        "aws_sdk_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates if a resource is included or excluded from the assessment.</p>"""
    source_type: NotRequired[
        "aws_sdk_resiliencehub.types.resource_source_type.ResourceSourceType"
    ]
    """<p>Type of input source.</p>"""
    parent_resource_name: NotRequired[
        "aws_sdk_resiliencehub.types.entity_name.EntityName"
    ]
    """<p>Name of the parent resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalResource) -> dict:
    out: dict = {}
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    import aws_sdk_resiliencehub.types.logical_resource_id

    out["logicalResourceId"] = (
        aws_sdk_resiliencehub.types.logical_resource_id.serialize_json(
            value["logical_resource_id"]
        )
    )
    import aws_sdk_resiliencehub.types.physical_resource_id

    out["physicalResourceId"] = (
        aws_sdk_resiliencehub.types.physical_resource_id.serialize_json(
            value["physical_resource_id"]
        )
    )
    out["resourceType"] = value["resource_type"]
    if "app_components" in value:
        import aws_sdk_resiliencehub.types.app_component_list

        out["appComponents"] = (
            aws_sdk_resiliencehub.types.app_component_list.serialize_json(
                value["app_components"]
            )
        )
    if "additional_info" in value:
        import aws_sdk_resiliencehub.types.additional_info_map

        out["additionalInfo"] = (
            aws_sdk_resiliencehub.types.additional_info_map.serialize_json(
                value["additional_info"]
            )
        )
    if "excluded" in value:
        out["excluded"] = value["excluded"]
    if "source_type" in value:
        import aws_sdk_resiliencehub.types.resource_source_type

        out["sourceType"] = (
            aws_sdk_resiliencehub.types.resource_source_type.serialize_json(
                value["source_type"]
            )
        )
    if "parent_resource_name" in value:
        out["parentResourceName"] = value["parent_resource_name"]
    return out


def deserialize_json(data: dict) -> PhysicalResource:
    out: PhysicalResource = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "logicalResourceId" in data:
        import aws_sdk_resiliencehub.types.logical_resource_id

        out["logical_resource_id"] = (
            aws_sdk_resiliencehub.types.logical_resource_id.deserialize_json(
                data["logicalResourceId"]
            )
        )
    else:
        raise DeserializationError("PhysicalResource.logical_resource_id required")
    if "physicalResourceId" in data:
        import aws_sdk_resiliencehub.types.physical_resource_id

        out["physical_resource_id"] = (
            aws_sdk_resiliencehub.types.physical_resource_id.deserialize_json(
                data["physicalResourceId"]
            )
        )
    else:
        raise DeserializationError("PhysicalResource.physical_resource_id required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("PhysicalResource.resource_type required")
    if "appComponents" in data:
        import aws_sdk_resiliencehub.types.app_component_list

        out["app_components"] = (
            aws_sdk_resiliencehub.types.app_component_list.deserialize_json(
                data["appComponents"]
            )
        )
    if "additionalInfo" in data:
        import aws_sdk_resiliencehub.types.additional_info_map

        out["additional_info"] = (
            aws_sdk_resiliencehub.types.additional_info_map.deserialize_json(
                data["additionalInfo"]
            )
        )
    if "excluded" in data:
        out["excluded"] = data["excluded"]
    if "sourceType" in data:
        import aws_sdk_resiliencehub.types.resource_source_type

        out["source_type"] = (
            aws_sdk_resiliencehub.types.resource_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    if "parentResourceName" in data:
        out["parent_resource_name"] = data["parentResourceName"]
    return out
