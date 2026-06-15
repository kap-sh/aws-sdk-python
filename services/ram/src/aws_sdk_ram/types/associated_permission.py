"""Generated from Smithy shape ``com.amazonaws.ram#AssociatedPermission``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean
    import aws_sdk_ram.types.date_time
    import aws_sdk_ram.types.permission_feature_set
    import aws_sdk_ram.types.string


class AssociatedPermission(TypedDict):
    arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the associated managed permission.</p>"""
    permission_version: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The version of the permission currently associated with the resource share.</p>"""
    default_version: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>Indicates whether the associated resource share is using the default version of the permission.</p>"""
    resource_type: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The resource type to which this permission applies.</p>"""
    status: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The current status of the association between the permission and the resource share. The following are the possible values:</p> <ul> <li> <p> <code>ATTACHABLE</code> – This permission or version can be associated with resource shares.</p> </li> <li> <p> <code>UNATTACHABLE</code> – This permission or version can't currently be associated with resource shares.</p> </li> <li> <p> <code>DELETING</code> – This permission or version is in the process of being deleted.</p> </li> <li> <p> <code>DELETED</code> – This permission or version is deleted.</p> </li> </ul>"""
    feature_set: NotRequired[
        "aws_sdk_ram.types.permission_feature_set.PermissionFeatureSet"
    ]
    """<p>Indicates what features are available for this resource share. This parameter can have one of the following values:</p> <ul> <li> <p> <b>STANDARD</b> – A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in RAM using the console or APIs. This resource share might have been created by RAM, or it might have been <b>CREATED_FROM_POLICY</b> and then promoted.</p> </li> <li> <p> <b>CREATED_FROM_POLICY</b> – The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so RAM created this customer managed permission automatically on the customer's behalf based on the attached policy document. This type of resource share is visible only to the Amazon Web Services account that created it. You can't modify it in RAM unless you promote it. For more information, see <a>PromoteResourceShareCreatedFromPolicy</a>.</p> </li> <li> <p> <b>PROMOTING_TO_STANDARD</b> – This resource share was originally <code>CREATED_FROM_POLICY</code>, but the customer ran the <a>PromoteResourceShareCreatedFromPolicy</a> and that operation is still in progress. This value changes to <code>STANDARD</code> when complete.</p> </li> </ul>"""
    last_updated_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the association between the permission and the resource share was last updated.</p>"""
    resource_share_arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of a resource share associated with this permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedPermission) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "permission_version" in value:
        out["permissionVersion"] = value["permission_version"]
    if "default_version" in value:
        out["defaultVersion"] = value["default_version"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "status" in value:
        out["status"] = value["status"]
    if "feature_set" in value:
        import aws_sdk_ram.types.permission_feature_set

        out["featureSet"] = aws_sdk_ram.types.permission_feature_set.serialize_json(
            value["feature_set"]
        )
    if "last_updated_time" in value:
        import aws_sdk_ram.types.date_time

        out["lastUpdatedTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["last_updated_time"]
        )
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    return out


def deserialize_json(data: dict) -> AssociatedPermission:
    out: AssociatedPermission = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "permissionVersion" in data:
        out["permission_version"] = data["permissionVersion"]
    if "defaultVersion" in data:
        out["default_version"] = data["defaultVersion"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "status" in data:
        out["status"] = data["status"]
    if "featureSet" in data:
        import aws_sdk_ram.types.permission_feature_set

        out["feature_set"] = aws_sdk_ram.types.permission_feature_set.deserialize_json(
            data["featureSet"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_ram.types.date_time

        out["last_updated_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["lastUpdatedTime"]
        )
    if "resourceShareArn" in data:
        out["resource_share_arn"] = data["resourceShareArn"]
    return out
