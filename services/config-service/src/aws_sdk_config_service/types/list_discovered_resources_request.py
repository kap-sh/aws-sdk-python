"""Generated from Smithy shape ``com.amazonaws.configservice#ListDiscoveredResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.boolean
    import aws_sdk_config_service.types.limit
    import aws_sdk_config_service.types.next_token
    import aws_sdk_config_service.types.resource_id_list
    import aws_sdk_config_service.types.resource_name
    import aws_sdk_config_service.types.resource_type


class ListDiscoveredResourcesRequest(TypedDict):
    resource_type: "aws_sdk_config_service.types.resource_type.ResourceType"
    """<p>The type of resources that you want Config to list in the response.</p>"""
    resource_ids: NotRequired[
        "aws_sdk_config_service.types.resource_id_list.ResourceIdList"
    ]
    """<p>The IDs of only those resources that you want Config to list in the response. If you do not specify this parameter, Config lists all resources of the specified type that it has discovered. You can list a minimum of 1 resourceID and a maximum of 20 resourceIds.</p>"""
    resource_name: NotRequired[
        "aws_sdk_config_service.types.resource_name.ResourceName"
    ]
    """<p>The custom name of only those resources that you want Config to list in the response. If you do not specify this parameter, Config lists all resources of the specified type that it has discovered.</p>"""
    limit: "aws_sdk_config_service.types.limit.Limit"
    """<p>The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    include_deleted_resources: "aws_sdk_config_service.types.boolean.Boolean"
    """<p>Specifies whether Config includes deleted resources in the results. By default, deleted resources are not included.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDiscoveredResourcesRequest) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.resource_type

    out["resourceType"] = (
        aws_sdk_config_service.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    if "resource_ids" in value:
        import aws_sdk_config_service.types.resource_id_list

        out["resourceIds"] = (
            aws_sdk_config_service.types.resource_id_list.serialize_aws_json_1_1(
                value["resource_ids"]
            )
        )
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    out["limit"] = value.get("limit", 0)
    out["includeDeletedResources"] = value.get("include_deleted_resources", False)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDiscoveredResourcesRequest:
    out: ListDiscoveredResourcesRequest = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_config_service.types.resource_type

        out["resource_type"] = (
            aws_sdk_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "ListDiscoveredResourcesRequest.resource_type required"
        )
    if "resourceIds" in data:
        import aws_sdk_config_service.types.resource_id_list

        out["resource_ids"] = (
            aws_sdk_config_service.types.resource_id_list.deserialize_aws_json_1_1(
                data["resourceIds"]
            )
        )
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    if "includeDeletedResources" in data:
        out["include_deleted_resources"] = data["includeDeletedResources"]
    else:
        out["include_deleted_resources"] = False
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
