"""Generated from Smithy shape ``com.amazonaws.ram#ResourceSharePermissionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean
    import aws_sdk_ram.types.date_time
    import aws_sdk_ram.types.permission_feature_set
    import aws_sdk_ram.types.permission_type
    import aws_sdk_ram.types.string
    import aws_sdk_ram.types.tag_list


class ResourceSharePermissionSummary(TypedDict):
    arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the permission you want information about.</p>"""
    version: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The version of the permission associated with this resource share.</p>"""
    default_version: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>Specifies whether the version of the managed permission used by this resource share is the default version for this managed permission.</p>"""
    name: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The name of this managed permission.</p>"""
    resource_type: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The type of resource to which this permission applies. This takes the form of: <code>service-code</code>:<code>resource-code</code>, and is case-insensitive. For example, an Amazon EC2 Subnet would be represented by the string <code>ec2:subnet</code>.</p>"""
    status: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The current status of the permission.</p>"""
    creation_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the permission was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the permission was last updated.</p>"""
    is_resource_type_default: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>Specifies whether the managed permission associated with this resource share is the default managed permission for all resources of this resource type.</p>"""
    permission_type: NotRequired["aws_sdk_ram.types.permission_type.PermissionType"]
    """<p>The type of managed permission. This can be one of the following values:</p> <ul> <li> <p> <code>AWS_MANAGED</code> – Amazon Web Services created and manages this managed permission. You can associate it with your resource shares, but you can't modify it.</p> </li> <li> <p> <code>CUSTOMER_MANAGED</code> – You, or another principal in your account created this managed permission. You can associate it with your resource shares and create new versions that have different permissions.</p> </li> </ul>"""
    feature_set: NotRequired[
        "aws_sdk_ram.types.permission_feature_set.PermissionFeatureSet"
    ]
    """<p>Indicates what features are available for this resource share. This parameter can have one of the following values:</p> <ul> <li> <p> <b>STANDARD</b> – A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in RAM using the console or APIs. This resource share might have been created by RAM, or it might have been <b>CREATED_FROM_POLICY</b> and then promoted.</p> </li> <li> <p> <b>CREATED_FROM_POLICY</b> – The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so RAM created this customer managed permission automatically on the customer's behalf based on the attached policy document. This type of resource share is visible only to the Amazon Web Services account that created it. You can't modify it in RAM unless you promote it. For more information, see <a>PromoteResourceShareCreatedFromPolicy</a>.</p> </li> <li> <p> <b>PROMOTING_TO_STANDARD</b> – This resource share was originally <code>CREATED_FROM_POLICY</code>, but the customer ran the <a>PromoteResourceShareCreatedFromPolicy</a> and that operation is still in progress. This value changes to <code>STANDARD</code> when complete.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_ram.types.tag_list.TagList"]
    """<p>A list of the tag key value pairs currently attached to the permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSharePermissionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "version" in value:
        out["version"] = value["version"]
    if "default_version" in value:
        out["defaultVersion"] = value["default_version"]
    if "name" in value:
        out["name"] = value["name"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_time" in value:
        import aws_sdk_ram.types.date_time

        out["creationTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_ram.types.date_time

        out["lastUpdatedTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["last_updated_time"]
        )
    if "is_resource_type_default" in value:
        out["isResourceTypeDefault"] = value["is_resource_type_default"]
    if "permission_type" in value:
        import aws_sdk_ram.types.permission_type

        out["permissionType"] = aws_sdk_ram.types.permission_type.serialize_json(
            value["permission_type"]
        )
    if "feature_set" in value:
        import aws_sdk_ram.types.permission_feature_set

        out["featureSet"] = aws_sdk_ram.types.permission_feature_set.serialize_json(
            value["feature_set"]
        )
    if "tags" in value:
        import aws_sdk_ram.types.tag_list

        out["tags"] = aws_sdk_ram.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ResourceSharePermissionSummary:
    out: ResourceSharePermissionSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "version" in data:
        out["version"] = data["version"]
    if "defaultVersion" in data:
        out["default_version"] = data["defaultVersion"]
    if "name" in data:
        out["name"] = data["name"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "status" in data:
        out["status"] = data["status"]
    if "creationTime" in data:
        import aws_sdk_ram.types.date_time

        out["creation_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_ram.types.date_time

        out["last_updated_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["lastUpdatedTime"]
        )
    if "isResourceTypeDefault" in data:
        out["is_resource_type_default"] = data["isResourceTypeDefault"]
    if "permissionType" in data:
        import aws_sdk_ram.types.permission_type

        out["permission_type"] = aws_sdk_ram.types.permission_type.deserialize_json(
            data["permissionType"]
        )
    if "featureSet" in data:
        import aws_sdk_ram.types.permission_feature_set

        out["feature_set"] = aws_sdk_ram.types.permission_feature_set.deserialize_json(
            data["featureSet"]
        )
    if "tags" in data:
        import aws_sdk_ram.types.tag_list

        out["tags"] = aws_sdk_ram.types.tag_list.deserialize_json(data["tags"])
    return out
