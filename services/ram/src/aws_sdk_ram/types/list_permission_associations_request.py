"""Generated from Smithy shape ``com.amazonaws.ram#ListPermissionAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean
    import aws_sdk_ram.types.integer
    import aws_sdk_ram.types.max_results
    import aws_sdk_ram.types.permission_feature_set
    import aws_sdk_ram.types.resource_share_association_status
    import aws_sdk_ram.types.string


class ListPermissionAssociationsRequest(TypedDict, closed=True):
    permission_arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the managed permission.</p>"""
    permission_version: NotRequired["aws_sdk_ram.types.integer.Integer"]
    """<p>Specifies that you want to list only those associations with resource shares that use this version of the managed permission. If you don't provide a value for this parameter, then the operation returns information about associations with resource shares that use any version of the managed permission.</p>"""
    association_status: NotRequired[
        "aws_sdk_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
    ]
    """<p>Specifies that you want to list only those associations with resource shares that match this status.</p>"""
    resource_type: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>Specifies that you want to list only those associations with resource shares that include at least one resource of this resource type.</p>"""
    feature_set: NotRequired[
        "aws_sdk_ram.types.permission_feature_set.PermissionFeatureSet"
    ]
    """<p>Specifies that you want to list only those associations with resource shares that have a <code>featureSet</code> with this value.</p>"""
    default_version: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>When <code>true</code>, specifies that you want to list only those associations with resource shares that use the default version of the specified managed permission.</p> <p>When <code>false</code> (the default value), lists associations with resource shares that use any version of the specified managed permission.</p>"""
    next_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionAssociationsRequest) -> dict:
    out: dict = {}
    if "permission_arn" in value:
        out["permissionArn"] = value["permission_arn"]
    if "permission_version" in value:
        out["permissionVersion"] = value["permission_version"]
    if "association_status" in value:
        import aws_sdk_ram.types.resource_share_association_status

        out["associationStatus"] = (
            aws_sdk_ram.types.resource_share_association_status.serialize_json(
                value["association_status"]
            )
        )
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "feature_set" in value:
        import aws_sdk_ram.types.permission_feature_set

        out["featureSet"] = aws_sdk_ram.types.permission_feature_set.serialize_json(
            value["feature_set"]
        )
    if "default_version" in value:
        out["defaultVersion"] = value["default_version"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListPermissionAssociationsRequest:
    out: ListPermissionAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "permissionArn" in data:
        out["permission_arn"] = data["permissionArn"]
    if "permissionVersion" in data:
        out["permission_version"] = data["permissionVersion"]
    if "associationStatus" in data:
        import aws_sdk_ram.types.resource_share_association_status

        out["association_status"] = (
            aws_sdk_ram.types.resource_share_association_status.deserialize_json(
                data["associationStatus"]
            )
        )
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "featureSet" in data:
        import aws_sdk_ram.types.permission_feature_set

        out["feature_set"] = aws_sdk_ram.types.permission_feature_set.deserialize_json(
            data["featureSet"]
        )
    if "defaultVersion" in data:
        out["default_version"] = data["defaultVersion"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
