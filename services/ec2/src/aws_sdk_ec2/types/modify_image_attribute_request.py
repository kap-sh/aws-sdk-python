"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyImageAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_value
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.launch_permission_modifications
    import aws_sdk_ec2.types.operation_type
    import aws_sdk_ec2.types.organization_arn_string_list
    import aws_sdk_ec2.types.organizational_unit_arn_string_list
    import aws_sdk_ec2.types.product_code_string_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_group_string_list
    import aws_sdk_ec2.types.user_id_string_list


class ModifyImageAttributeRequest(TypedDict, closed=True):
    attribute: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the attribute to modify.</p> <p>Valid values: <code>description</code> | <code>imdsSupport</code> | <code>launchPermission</code> </p>"""
    description: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>A new description for the AMI.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    launch_permission: NotRequired[
        "aws_sdk_ec2.types.launch_permission_modifications.LaunchPermissionModifications"
    ]
    """<p>A new launch permission for the AMI.</p>"""
    operation_type: NotRequired["aws_sdk_ec2.types.operation_type.OperationType"]
    """<p>The operation type. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    product_codes: NotRequired[
        "aws_sdk_ec2.types.product_code_string_list.ProductCodeStringList"
    ]
    """<p>Not supported.</p>"""
    user_groups: NotRequired[
        "aws_sdk_ec2.types.user_group_string_list.UserGroupStringList"
    ]
    """<p>The user groups. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    user_ids: NotRequired["aws_sdk_ec2.types.user_id_string_list.UserIdStringList"]
    """<p>The Amazon Web Services account IDs. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value of the attribute being modified. This parameter can be used only when the <code>Attribute</code> parameter is <code>description</code> or <code>imdsSupport</code>.</p>"""
    organization_arns: NotRequired[
        "aws_sdk_ec2.types.organization_arn_string_list.OrganizationArnStringList"
    ]
    """<p>The Amazon Resource Name (ARN) of an organization. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    organizational_unit_arns: NotRequired[
        "aws_sdk_ec2.types.organizational_unit_arn_string_list.OrganizationalUnitArnStringList"
    ]
    """<p>The Amazon Resource Name (ARN) of an organizational unit (OU). This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    imds_support: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    r"""<p>Set to <code>v2.0</code> to indicate that IMDSv2 is specified in the AMI. Instances launched from this AMI will have <code>HttpTokens</code> automatically set to <code>required</code> so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, <code>HttpPutResponseHopLimit</code> is set to <code>2</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration\">Configure the AMI</a> in the <i>Amazon EC2 User Guide</i>.</p> <important> <p>Do not use this parameter unless your AMI software supports IMDSv2. After you set the value to <code>v2.0</code>, you can't undo it. The only way to “reset” your AMI is to create a new AMI from the underlying snapshot.</p> </important>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyImageAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute" in value:
        pairs.append((f"{prefix}.Attribute", str(value["attribute"])))
    if "description" in value:
        import aws_sdk_ec2.types.attribute_value

        aws_sdk_ec2.types.attribute_value.serialize_ec2_query(
            value["description"], pairs, f"{prefix}.Description"
        )
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "launch_permission" in value:
        import aws_sdk_ec2.types.launch_permission_modifications

        aws_sdk_ec2.types.launch_permission_modifications.serialize_ec2_query(
            value["launch_permission"], pairs, f"{prefix}.LaunchPermission"
        )
    if "operation_type" in value:
        import aws_sdk_ec2.types.operation_type

        aws_sdk_ec2.types.operation_type.serialize_ec2_query(
            value["operation_type"], pairs, f"{prefix}.OperationType"
        )
    if "product_codes" in value:
        import aws_sdk_ec2.types.product_code_string_list

        aws_sdk_ec2.types.product_code_string_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{prefix}.ProductCodes"
        )
    if "user_groups" in value:
        import aws_sdk_ec2.types.user_group_string_list

        aws_sdk_ec2.types.user_group_string_list.serialize_ec2_query(
            value["user_groups"], pairs, f"{prefix}.UserGroups"
        )
    if "user_ids" in value:
        import aws_sdk_ec2.types.user_id_string_list

        aws_sdk_ec2.types.user_id_string_list.serialize_ec2_query(
            value["user_ids"], pairs, f"{prefix}.UserIds"
        )
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))
    if "organization_arns" in value:
        import aws_sdk_ec2.types.organization_arn_string_list

        aws_sdk_ec2.types.organization_arn_string_list.serialize_ec2_query(
            value["organization_arns"], pairs, f"{prefix}.OrganizationArns"
        )
    if "organizational_unit_arns" in value:
        import aws_sdk_ec2.types.organizational_unit_arn_string_list

        aws_sdk_ec2.types.organizational_unit_arn_string_list.serialize_ec2_query(
            value["organizational_unit_arns"], pairs, f"{prefix}.OrganizationalUnitArns"
        )
    if "imds_support" in value:
        import aws_sdk_ec2.types.attribute_value

        aws_sdk_ec2.types.attribute_value.serialize_ec2_query(
            value["imds_support"], pairs, f"{prefix}.ImdsSupport"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyImageAttributeRequest:
    out: ModifyImageAttributeRequest = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        out["attribute"] = str(child_attribute.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        import aws_sdk_ec2.types.attribute_value

        out["description"] = aws_sdk_ec2.types.attribute_value.deserialize_ec2_query(
            child_description
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_launch_permission = el.find("LaunchPermission")
    if child_launch_permission is not None:
        import aws_sdk_ec2.types.launch_permission_modifications

        out["launch_permission"] = (
            aws_sdk_ec2.types.launch_permission_modifications.deserialize_ec2_query(
                child_launch_permission
            )
        )
    child_operation_type = el.find("OperationType")
    if child_operation_type is not None:
        import aws_sdk_ec2.types.operation_type

        out["operation_type"] = aws_sdk_ec2.types.operation_type.deserialize_ec2_query(
            child_operation_type
        )
    if el.find("ProductCodes") is not None:
        import aws_sdk_ec2.types.product_code_string_list

        out["product_codes"] = (
            aws_sdk_ec2.types.product_code_string_list.deserialize_ec2_query(
                el, "ProductCodes"
            )
        )
    if el.find("UserGroups") is not None:
        import aws_sdk_ec2.types.user_group_string_list

        out["user_groups"] = (
            aws_sdk_ec2.types.user_group_string_list.deserialize_ec2_query(
                el, "UserGroups"
            )
        )
    if el.find("UserIds") is not None:
        import aws_sdk_ec2.types.user_id_string_list

        out["user_ids"] = aws_sdk_ec2.types.user_id_string_list.deserialize_ec2_query(
            el, "UserIds"
        )
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    if el.find("OrganizationArns") is not None:
        import aws_sdk_ec2.types.organization_arn_string_list

        out["organization_arns"] = (
            aws_sdk_ec2.types.organization_arn_string_list.deserialize_ec2_query(
                el, "OrganizationArns"
            )
        )
    if el.find("OrganizationalUnitArns") is not None:
        import aws_sdk_ec2.types.organizational_unit_arn_string_list

        out["organizational_unit_arns"] = (
            aws_sdk_ec2.types.organizational_unit_arn_string_list.deserialize_ec2_query(
                el, "OrganizationalUnitArns"
            )
        )
    child_imds_support = el.find("ImdsSupport")
    if child_imds_support is not None:
        import aws_sdk_ec2.types.attribute_value

        out["imds_support"] = aws_sdk_ec2.types.attribute_value.deserialize_ec2_query(
            child_imds_support
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
