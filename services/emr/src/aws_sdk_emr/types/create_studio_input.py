"""Generated from Smithy shape ``com.amazonaws.emr#CreateStudioInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.arn_type
    import aws_sdk_emr.types.auth_mode
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.idc_user_assignment
    import aws_sdk_emr.types.subnet_id_list
    import aws_sdk_emr.types.tag_list
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256


class CreateStudioInput(TypedDict, closed=True):
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>A descriptive name for the Amazon EMR Studio.</p>"""
    description: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>A detailed description of the Amazon EMR Studio.</p>"""
    auth_mode: NotRequired["aws_sdk_emr.types.auth_mode.AuthMode"]
    """<p>Specifies whether the Studio authenticates users using IAM or IAM Identity Center.</p>"""
    vpc_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.</p>"""
    subnet_ids: NotRequired["aws_sdk_emr.types.subnet_id_list.SubnetIdList"]
    """<p>A list of subnet IDs to associate with the Amazon EMR Studio. A Studio can have a maximum of 5 subnets. The subnets must belong to the VPC specified by <code>VpcId</code>. Studio users can create a Workspace in any of the specified subnets.</p>"""
    service_role: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The IAM role that the Amazon EMR Studio assumes. The service role provides a way for Amazon EMR Studio to interoperate with other Amazon Web Services services.</p>"""
    user_role: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The IAM user role that users and groups assume when logged in to an Amazon EMR Studio. Only specify a <code>UserRole</code> when you use IAM Identity Center authentication. The permissions attached to the <code>UserRole</code> can be scoped down for each user or group using session policies.</p>"""
    workspace_security_group_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by <code>VpcId</code>.</p>"""
    engine_security_group_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by <code>VpcId</code>.</p>"""
    default_s3_location: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The Amazon S3 location to back up Amazon EMR Studio Workspaces and notebook files.</p>"""
    idp_auth_url: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The authentication endpoint of your identity provider (IdP). Specify this value when you use IAM authentication and want to let federated users log in to a Studio with the Studio URL and credentials from your IdP. Amazon EMR Studio redirects users to this endpoint to enter credentials.</p>"""
    idp_relay_state_parameter_name: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The name that your identity provider (IdP) uses for its <code>RelayState</code> parameter. For example, <code>RelayState</code> or <code>TargetSource</code>. Specify this value when you use IAM authentication and want to let federated users log in to a Studio using the Studio URL. The <code>RelayState</code> parameter differs by IdP.</p>"""
    tags: NotRequired["aws_sdk_emr.types.tag_list.TagList"]
    """<p>A list of tags to associate with the Amazon EMR Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.</p>"""
    trusted_identity_propagation_enabled: NotRequired[
        "aws_sdk_emr.types.boolean_object.BooleanObject"
    ]
    """<p> A Boolean indicating whether to enable Trusted identity propagation for the Studio. The default value is <code>false</code>. </p>"""
    idc_user_assignment: NotRequired[
        "aws_sdk_emr.types.idc_user_assignment.IdcUserAssignment"
    ]
    """<p> Specifies whether IAM Identity Center user assignment is <code>REQUIRED</code> or <code>OPTIONAL</code>. If the value is set to <code>REQUIRED</code>, users must be explicitly assigned to the Studio application to access the Studio. </p>"""
    idc_instance_arn: NotRequired["aws_sdk_emr.types.arn_type.ArnType"]
    """<p> The ARN of the IAM Identity Center instance to create the Studio application. </p>"""
    encryption_key_arn: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStudioInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "auth_mode" in value:
        import aws_sdk_emr.types.auth_mode

        out["AuthMode"] = aws_sdk_emr.types.auth_mode.serialize_aws_json_1_1(
            value["auth_mode"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_emr.types.subnet_id_list

        out["SubnetIds"] = aws_sdk_emr.types.subnet_id_list.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "user_role" in value:
        out["UserRole"] = value["user_role"]
    if "workspace_security_group_id" in value:
        out["WorkspaceSecurityGroupId"] = value["workspace_security_group_id"]
    if "engine_security_group_id" in value:
        out["EngineSecurityGroupId"] = value["engine_security_group_id"]
    if "default_s3_location" in value:
        out["DefaultS3Location"] = value["default_s3_location"]
    if "idp_auth_url" in value:
        out["IdpAuthUrl"] = value["idp_auth_url"]
    if "idp_relay_state_parameter_name" in value:
        out["IdpRelayStateParameterName"] = value["idp_relay_state_parameter_name"]
    if "tags" in value:
        import aws_sdk_emr.types.tag_list

        out["Tags"] = aws_sdk_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "trusted_identity_propagation_enabled" in value:
        out["TrustedIdentityPropagationEnabled"] = value[
            "trusted_identity_propagation_enabled"
        ]
    if "idc_user_assignment" in value:
        import aws_sdk_emr.types.idc_user_assignment

        out["IdcUserAssignment"] = (
            aws_sdk_emr.types.idc_user_assignment.serialize_aws_json_1_1(
                value["idc_user_assignment"]
            )
        )
    if "idc_instance_arn" in value:
        out["IdcInstanceArn"] = value["idc_instance_arn"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStudioInput:
    out: CreateStudioInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "AuthMode" in data:
        import aws_sdk_emr.types.auth_mode

        out["auth_mode"] = aws_sdk_emr.types.auth_mode.deserialize_aws_json_1_1(
            data["AuthMode"]
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetIds" in data:
        import aws_sdk_emr.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_emr.types.subnet_id_list.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if "ServiceRole" in data:
        out["service_role"] = data["ServiceRole"]
    if "UserRole" in data:
        out["user_role"] = data["UserRole"]
    if "WorkspaceSecurityGroupId" in data:
        out["workspace_security_group_id"] = data["WorkspaceSecurityGroupId"]
    if "EngineSecurityGroupId" in data:
        out["engine_security_group_id"] = data["EngineSecurityGroupId"]
    if "DefaultS3Location" in data:
        out["default_s3_location"] = data["DefaultS3Location"]
    if "IdpAuthUrl" in data:
        out["idp_auth_url"] = data["IdpAuthUrl"]
    if "IdpRelayStateParameterName" in data:
        out["idp_relay_state_parameter_name"] = data["IdpRelayStateParameterName"]
    if "Tags" in data:
        import aws_sdk_emr.types.tag_list

        out["tags"] = aws_sdk_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "TrustedIdentityPropagationEnabled" in data:
        out["trusted_identity_propagation_enabled"] = data[
            "TrustedIdentityPropagationEnabled"
        ]
    if "IdcUserAssignment" in data:
        import aws_sdk_emr.types.idc_user_assignment

        out["idc_user_assignment"] = (
            aws_sdk_emr.types.idc_user_assignment.deserialize_aws_json_1_1(
                data["IdcUserAssignment"]
            )
        )
    if "IdcInstanceArn" in data:
        out["idc_instance_arn"] = data["IdcInstanceArn"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    return out
