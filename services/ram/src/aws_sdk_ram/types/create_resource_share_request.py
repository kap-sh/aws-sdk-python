"""Generated from Smithy shape ``com.amazonaws.ram#CreateResourceShareRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ram.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean
    import aws_sdk_ram.types.permission_arn_list
    import aws_sdk_ram.types.principal_arn_or_id_list
    import aws_sdk_ram.types.resource_arn_list
    import aws_sdk_ram.types.resource_share_configuration
    import aws_sdk_ram.types.source_arn_or_account_list
    import aws_sdk_ram.types.string
    import aws_sdk_ram.types.tag_list


class CreateResourceShareRequest(TypedDict):
    name: "aws_sdk_ram.types.string.String"
    """<p>Specifies the name of the resource share.</p>"""
    resource_arns: NotRequired["aws_sdk_ram.types.resource_arn_list.ResourceArnList"]
    """<p>Specifies a list of one or more ARNs of the resources to associate with the resource share.</p>"""
    principals: NotRequired[
        "aws_sdk_ram.types.principal_arn_or_id_list.PrincipalArnOrIdList"
    ]
    """<p>Specifies a list of one or more principals to associate with the resource share.</p> <p>You can include the following values:</p> <ul> <li> <p>An Amazon Web Services account ID, for example: <code>123456789012</code> </p> </li> <li> <p>An <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of an organization in Organizations, for example: <code>organizations::123456789012:organization/o-exampleorgid</code> </p> </li> <li> <p>An ARN of an organizational unit (OU) in Organizations, for example: <code>organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123</code> </p> </li> <li> <p>An ARN of an IAM role, for example: <code>iam::123456789012:role/rolename</code> </p> </li> <li> <p>An ARN of an IAM user, for example: <code>iam::123456789012user/username</code> </p> </li> <li> <p>A service principal name, for example: <code>service-id.amazonaws.com</code> </p> </li> </ul> <note> <p>Not all resource types can be shared with IAM roles and users. For more information, see <a href=\"https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types\">Sharing with IAM roles and users</a> in the <i>Resource Access Manager User Guide</i>.</p> </note>"""
    tags: NotRequired["aws_sdk_ram.types.tag_list.TagList"]
    """<p>Specifies one or more tags to attach to the resource share itself. It doesn't attach the tags to the resources associated with the resource share.</p>"""
    allow_external_principals: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>Specifies whether principals outside your organization in Organizations can be associated with a resource share. A value of <code>true</code> lets you share with individual Amazon Web Services accounts that are <i>not</i> in your organization. A value of <code>false</code> only has meaning if your account is a member of an Amazon Web Services Organization. The default value is <code>true</code>.</p>"""
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    permission_arns: NotRequired[
        "aws_sdk_ram.types.permission_arn_list.PermissionArnList"
    ]
    """<p>Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> of the RAM permission to associate with the resource share. If you do not specify an ARN for the permission, RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.</p>"""
    sources: NotRequired[
        "aws_sdk_ram.types.source_arn_or_account_list.SourceArnOrAccountList"
    ]
    """<p>Specifies source constraints (accounts, ARNs, organization IDs, or organization paths) that limit when service principals can access resources in this resource share. When a service principal attempts to access a shared resource, validation is performed to ensure the request originates from one of the specified sources. This helps prevent confused deputy attacks by applying constraints on where service principals can access resources from.</p>"""
    resource_share_configuration: NotRequired[
        "aws_sdk_ram.types.resource_share_configuration.ResourceShareConfiguration"
    ]
    """<p>Specifies the configuration of this resource share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceShareRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "resource_arns" in value:
        import aws_sdk_ram.types.resource_arn_list

        out["resourceArns"] = aws_sdk_ram.types.resource_arn_list.serialize_json(
            value["resource_arns"]
        )
    if "principals" in value:
        import aws_sdk_ram.types.principal_arn_or_id_list

        out["principals"] = aws_sdk_ram.types.principal_arn_or_id_list.serialize_json(
            value["principals"]
        )
    if "tags" in value:
        import aws_sdk_ram.types.tag_list

        out["tags"] = aws_sdk_ram.types.tag_list.serialize_json(value["tags"])
    if "allow_external_principals" in value:
        out["allowExternalPrincipals"] = value["allow_external_principals"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "permission_arns" in value:
        import aws_sdk_ram.types.permission_arn_list

        out["permissionArns"] = aws_sdk_ram.types.permission_arn_list.serialize_json(
            value["permission_arns"]
        )
    if "sources" in value:
        import aws_sdk_ram.types.source_arn_or_account_list

        out["sources"] = aws_sdk_ram.types.source_arn_or_account_list.serialize_json(
            value["sources"]
        )
    if "resource_share_configuration" in value:
        import aws_sdk_ram.types.resource_share_configuration

        out["resourceShareConfiguration"] = (
            aws_sdk_ram.types.resource_share_configuration.serialize_json(
                value["resource_share_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateResourceShareRequest:
    out: CreateResourceShareRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateResourceShareRequest.name required")
    if "resourceArns" in data:
        import aws_sdk_ram.types.resource_arn_list

        out["resource_arns"] = aws_sdk_ram.types.resource_arn_list.deserialize_json(
            data["resourceArns"]
        )
    if "principals" in data:
        import aws_sdk_ram.types.principal_arn_or_id_list

        out["principals"] = aws_sdk_ram.types.principal_arn_or_id_list.deserialize_json(
            data["principals"]
        )
    if "tags" in data:
        import aws_sdk_ram.types.tag_list

        out["tags"] = aws_sdk_ram.types.tag_list.deserialize_json(data["tags"])
    if "allowExternalPrincipals" in data:
        out["allow_external_principals"] = data["allowExternalPrincipals"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "permissionArns" in data:
        import aws_sdk_ram.types.permission_arn_list

        out["permission_arns"] = aws_sdk_ram.types.permission_arn_list.deserialize_json(
            data["permissionArns"]
        )
    if "sources" in data:
        import aws_sdk_ram.types.source_arn_or_account_list

        out["sources"] = aws_sdk_ram.types.source_arn_or_account_list.deserialize_json(
            data["sources"]
        )
    if "resourceShareConfiguration" in data:
        import aws_sdk_ram.types.resource_share_configuration

        out["resource_share_configuration"] = (
            aws_sdk_ram.types.resource_share_configuration.deserialize_json(
                data["resourceShareConfiguration"]
            )
        )
    return out
