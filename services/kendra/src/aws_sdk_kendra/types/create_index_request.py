"""Generated from Smithy shape ``com.amazonaws.kendra#CreateIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.client_token_name
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.index_edition
    import aws_sdk_kendra.types.index_name
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.server_side_encryption_configuration
    import aws_sdk_kendra.types.tag_list
    import aws_sdk_kendra.types.user_context_policy
    import aws_sdk_kendra.types.user_group_resolution_configuration
    import aws_sdk_kendra.types.user_token_configuration_list


class CreateIndexRequest(TypedDict):
    name: "aws_sdk_kendra.types.index_name.IndexName"
    """<p>A name for the index.</p>"""
    edition: NotRequired["aws_sdk_kendra.types.index_edition.IndexEdition"]
    """<p>The Amazon Kendra edition to use for the index. Choose <code>DEVELOPER_EDITION</code> for indexes intended for development, testing, or proof of concept. Use <code>ENTERPRISE_EDITION</code> for production. Use <code>GEN_AI_ENTERPRISE_EDITION</code> for creating generative AI applications. Once you set the edition for an index, it can't be changed. </p> <p>The <code>Edition</code> parameter is optional. If you don't supply a value, the default is <code>ENTERPRISE_EDITION</code>.</p> <p>For more information on quota limits for Gen AI Enterprise Edition, Enterprise Edition, and Developer Edition indices, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/quotas.html\">Quotas</a>.</p>"""
    role_arn: "aws_sdk_kendra.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access your Amazon CloudWatch logs and metrics. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html\">IAM access roles for Amazon Kendra</a>.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_kendra.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The identifier of the KMS customer managed key (CMK) that's used to encrypt data indexed by Amazon Kendra. Amazon Kendra doesn't support asymmetric CMKs.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A description for the index.</p>"""
    client_token: NotRequired["aws_sdk_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create an index. Multiple calls to the <code>CreateIndex</code> API with the same client token will create only one index.</p>"""
    tags: NotRequired["aws_sdk_kendra.types.tag_list.TagList"]
    """<p>A list of key-value pairs that identify or categorize the index. You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    user_token_configurations: NotRequired[
        "aws_sdk_kendra.types.user_token_configuration_list.UserTokenConfigurationList"
    ]
    """<p>The user token configuration.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>UserTokenConfigurations</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>"""
    user_context_policy: NotRequired[
        "aws_sdk_kendra.types.user_context_policy.UserContextPolicy"
    ]
    """<p>The user context policy.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can only use <code>ATTRIBUTE_FILTER</code> to filter search results by user context. If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>USER_TOKEN</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important> <dl> <dt>ATTRIBUTE_FILTER</dt> <dd> <p>All indexed content is searchable and displayable for all users. If you want to filter search results on user context, you can use the attribute filters of <code>_user_id</code> and <code>_group_ids</code> or you can provide user and group information in <code>UserContext</code>. </p> </dd> <dt>USER_TOKEN</dt> <dd> <p>Enables token-based user access control to filter search results on user context. All documents with no access control and all documents accessible to the user will be searchable and displayable. </p> </dd> </dl>"""
    user_group_resolution_configuration: NotRequired[
        "aws_sdk_kendra.types.user_group_resolution_configuration.UserGroupResolutionConfiguration"
    ]
    """<p>Gets users and groups from IAM Identity Center identity source. To configure this, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_UserGroupResolutionConfiguration.html\">UserGroupResolutionConfiguration</a>. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, <code>UserGroupResolutionConfiguration</code> isn't supported.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIndexRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "edition" in value:
        import aws_sdk_kendra.types.index_edition

        out["Edition"] = aws_sdk_kendra.types.index_edition.serialize_aws_json_1_1(
            value["edition"]
        )
    out["RoleArn"] = value["role_arn"]
    if "server_side_encryption_configuration" in value:
        import aws_sdk_kendra.types.server_side_encryption_configuration

        out["ServerSideEncryptionConfiguration"] = (
            aws_sdk_kendra.types.server_side_encryption_configuration.serialize_aws_json_1_1(
                value["server_side_encryption_configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_kendra.types.tag_list

        out["Tags"] = aws_sdk_kendra.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "user_token_configurations" in value:
        import aws_sdk_kendra.types.user_token_configuration_list

        out["UserTokenConfigurations"] = (
            aws_sdk_kendra.types.user_token_configuration_list.serialize_aws_json_1_1(
                value["user_token_configurations"]
            )
        )
    if "user_context_policy" in value:
        import aws_sdk_kendra.types.user_context_policy

        out["UserContextPolicy"] = (
            aws_sdk_kendra.types.user_context_policy.serialize_aws_json_1_1(
                value["user_context_policy"]
            )
        )
    if "user_group_resolution_configuration" in value:
        import aws_sdk_kendra.types.user_group_resolution_configuration

        out["UserGroupResolutionConfiguration"] = (
            aws_sdk_kendra.types.user_group_resolution_configuration.serialize_aws_json_1_1(
                value["user_group_resolution_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIndexRequest:
    out: CreateIndexRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateIndexRequest.name required")
    if "Edition" in data:
        import aws_sdk_kendra.types.index_edition

        out["edition"] = aws_sdk_kendra.types.index_edition.deserialize_aws_json_1_1(
            data["Edition"]
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateIndexRequest.role_arn required")
    if "ServerSideEncryptionConfiguration" in data:
        import aws_sdk_kendra.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_kendra.types.server_side_encryption_configuration.deserialize_aws_json_1_1(
                data["ServerSideEncryptionConfiguration"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_kendra.types.tag_list

        out["tags"] = aws_sdk_kendra.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "UserTokenConfigurations" in data:
        import aws_sdk_kendra.types.user_token_configuration_list

        out["user_token_configurations"] = (
            aws_sdk_kendra.types.user_token_configuration_list.deserialize_aws_json_1_1(
                data["UserTokenConfigurations"]
            )
        )
    if "UserContextPolicy" in data:
        import aws_sdk_kendra.types.user_context_policy

        out["user_context_policy"] = (
            aws_sdk_kendra.types.user_context_policy.deserialize_aws_json_1_1(
                data["UserContextPolicy"]
            )
        )
    if "UserGroupResolutionConfiguration" in data:
        import aws_sdk_kendra.types.user_group_resolution_configuration

        out["user_group_resolution_configuration"] = (
            aws_sdk_kendra.types.user_group_resolution_configuration.deserialize_aws_json_1_1(
                data["UserGroupResolutionConfiguration"]
            )
        )
    return out
