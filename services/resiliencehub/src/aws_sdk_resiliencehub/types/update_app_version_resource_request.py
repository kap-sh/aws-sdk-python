"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateAppVersionResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.additional_info_map
    import aws_sdk_resiliencehub.types.app_component_name_list
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.aws_region
    import aws_sdk_resiliencehub.types.boolean_optional
    import aws_sdk_resiliencehub.types.customer_id
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.logical_resource_id
    import aws_sdk_resiliencehub.types.string255
    import aws_sdk_resiliencehub.types.string2048


class UpdateAppVersionResourceRequest(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    resource_name: NotRequired["aws_sdk_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the resource.</p>"""
    logical_resource_id: NotRequired[
        "aws_sdk_resiliencehub.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>Logical identifier of the resource.</p>"""
    physical_resource_id: NotRequired[
        "aws_sdk_resiliencehub.types.string2048.String2048"
    ]
    """<p>Physical identifier of the resource.</p>"""
    aws_region: NotRequired["aws_sdk_resiliencehub.types.aws_region.AwsRegion"]
    """<p>Amazon Web Services region that owns the physical resource.</p>"""
    aws_account_id: NotRequired["aws_sdk_resiliencehub.types.customer_id.CustomerId"]
    """<p>Amazon Web Services account that owns the physical resource.</p>"""
    resource_type: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Type of resource.</p>"""
    app_components: NotRequired[
        "aws_sdk_resiliencehub.types.app_component_name_list.AppComponentNameList"
    ]
    """<p>List of Application Components that this resource belongs to. If an Application Component is not part of the Resilience Hub application, it will be added.</p>"""
    additional_info: NotRequired[
        "aws_sdk_resiliencehub.types.additional_info_map.AdditionalInfoMap"
    ]
    """<p>Currently, there is no supported additional information for resources.</p>"""
    excluded: NotRequired[
        "aws_sdk_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates if a resource is excluded from an Resilience Hub application.</p> <note> <p>You can exclude only imported resources from an Resilience Hub application.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppVersionResourceRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "logical_resource_id" in value:
        import aws_sdk_resiliencehub.types.logical_resource_id

        out["logicalResourceId"] = (
            aws_sdk_resiliencehub.types.logical_resource_id.serialize_json(
                value["logical_resource_id"]
            )
        )
    if "physical_resource_id" in value:
        out["physicalResourceId"] = value["physical_resource_id"]
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "app_components" in value:
        import aws_sdk_resiliencehub.types.app_component_name_list

        out["appComponents"] = (
            aws_sdk_resiliencehub.types.app_component_name_list.serialize_json(
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
    return out


def deserialize_json(data: dict) -> UpdateAppVersionResourceRequest:
    out: UpdateAppVersionResourceRequest = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("UpdateAppVersionResourceRequest.app_arn required")
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "logicalResourceId" in data:
        import aws_sdk_resiliencehub.types.logical_resource_id

        out["logical_resource_id"] = (
            aws_sdk_resiliencehub.types.logical_resource_id.deserialize_json(
                data["logicalResourceId"]
            )
        )
    if "physicalResourceId" in data:
        out["physical_resource_id"] = data["physicalResourceId"]
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "appComponents" in data:
        import aws_sdk_resiliencehub.types.app_component_name_list

        out["app_components"] = (
            aws_sdk_resiliencehub.types.app_component_name_list.deserialize_json(
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
    return out
