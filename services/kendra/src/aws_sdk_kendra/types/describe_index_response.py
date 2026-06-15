"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeIndexResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.capacity_units_configuration
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.document_metadata_configuration_list
    import aws_sdk_kendra.types.error_message
    import aws_sdk_kendra.types.index_edition
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.index_name
    import aws_sdk_kendra.types.index_statistics
    import aws_sdk_kendra.types.index_status
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.server_side_encryption_configuration
    import aws_sdk_kendra.types.timestamp
    import aws_sdk_kendra.types.user_context_policy
    import aws_sdk_kendra.types.user_group_resolution_configuration
    import aws_sdk_kendra.types.user_token_configuration_list


class DescribeIndexResponse(TypedDict):
    name: NotRequired["aws_sdk_kendra.types.index_name.IndexName"]
    """<p>The name of the index.</p>"""
    id: NotRequired["aws_sdk_kendra.types.index_id.IndexId"]
    """<p>The identifier of the index.</p>"""
    edition: NotRequired["aws_sdk_kendra.types.index_edition.IndexEdition"]
    """<p>The Amazon Kendra edition used for the index. You decide the edition when you create the index.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that gives Amazon Kendra permission to write to your Amazon CloudWatch logs.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_kendra.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The identifier of the KMS customer master key (CMK) that is used to encrypt your data. Amazon Kendra doesn't support asymmetric CMKs.</p>"""
    status: NotRequired["aws_sdk_kendra.types.index_status.IndexStatus"]
    """<p>The current status of the index. When the value is <code>ACTIVE</code>, the index is ready for use. If the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>The description for the index.</p>"""
    created_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the index was created.</p>"""
    updated_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the index was last updated.</p>"""
    document_metadata_configurations: NotRequired[
        "aws_sdk_kendra.types.document_metadata_configuration_list.DocumentMetadataConfigurationList"
    ]
    """<p>Configuration information for document metadata or fields. Document metadata are fields or attributes associated with your documents. For example, the company department name associated with each document.</p>"""
    index_statistics: NotRequired[
        "aws_sdk_kendra.types.index_statistics.IndexStatistics"
    ]
    """<p>Provides information about the number of FAQ questions and answers and the number of text documents indexed.</p>"""
    error_message: NotRequired["aws_sdk_kendra.types.error_message.ErrorMessage"]
    """<p>When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""
    capacity_units: NotRequired[
        "aws_sdk_kendra.types.capacity_units_configuration.CapacityUnitsConfiguration"
    ]
    r"""<p>For Enterprise Edition indexes, you can choose to use additional capacity to meet the needs of your application. This contains the capacity units used for the index. A query or document storage capacity of zero indicates that the index is using the default capacity. For more information on the default capacity for an index and adjusting this, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html\">Adjusting capacity</a>.</p>"""
    user_token_configurations: NotRequired[
        "aws_sdk_kendra.types.user_token_configuration_list.UserTokenConfigurationList"
    ]
    """<p>The user token configuration for the Amazon Kendra index.</p>"""
    user_context_policy: NotRequired[
        "aws_sdk_kendra.types.user_context_policy.UserContextPolicy"
    ]
    """<p>The user context policy for the Amazon Kendra index.</p>"""
    user_group_resolution_configuration: NotRequired[
        "aws_sdk_kendra.types.user_group_resolution_configuration.UserGroupResolutionConfiguration"
    ]
    """<p>Whether you have enabled IAM Identity Center identity source for your users and groups. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIndexResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "edition" in value:
        import aws_sdk_kendra.types.index_edition

        out["Edition"] = aws_sdk_kendra.types.index_edition.serialize_aws_json_1_1(
            value["edition"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "server_side_encryption_configuration" in value:
        import aws_sdk_kendra.types.server_side_encryption_configuration

        out["ServerSideEncryptionConfiguration"] = (
            aws_sdk_kendra.types.server_side_encryption_configuration.serialize_aws_json_1_1(
                value["server_side_encryption_configuration"]
            )
        )
    if "status" in value:
        import aws_sdk_kendra.types.index_status

        out["Status"] = aws_sdk_kendra.types.index_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["CreatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["UpdatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "document_metadata_configurations" in value:
        import aws_sdk_kendra.types.document_metadata_configuration_list

        out["DocumentMetadataConfigurations"] = (
            aws_sdk_kendra.types.document_metadata_configuration_list.serialize_aws_json_1_1(
                value["document_metadata_configurations"]
            )
        )
    if "index_statistics" in value:
        import aws_sdk_kendra.types.index_statistics

        out["IndexStatistics"] = (
            aws_sdk_kendra.types.index_statistics.serialize_aws_json_1_1(
                value["index_statistics"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "capacity_units" in value:
        import aws_sdk_kendra.types.capacity_units_configuration

        out["CapacityUnits"] = (
            aws_sdk_kendra.types.capacity_units_configuration.serialize_aws_json_1_1(
                value["capacity_units"]
            )
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


def deserialize_aws_json_1_1(data: dict) -> DescribeIndexResponse:
    out: DescribeIndexResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Edition" in data:
        import aws_sdk_kendra.types.index_edition

        out["edition"] = aws_sdk_kendra.types.index_edition.deserialize_aws_json_1_1(
            data["Edition"]
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ServerSideEncryptionConfiguration" in data:
        import aws_sdk_kendra.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_kendra.types.server_side_encryption_configuration.deserialize_aws_json_1_1(
                data["ServerSideEncryptionConfiguration"]
            )
        )
    if "Status" in data:
        import aws_sdk_kendra.types.index_status

        out["status"] = aws_sdk_kendra.types.index_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["created_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["updated_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if "DocumentMetadataConfigurations" in data:
        import aws_sdk_kendra.types.document_metadata_configuration_list

        out["document_metadata_configurations"] = (
            aws_sdk_kendra.types.document_metadata_configuration_list.deserialize_aws_json_1_1(
                data["DocumentMetadataConfigurations"]
            )
        )
    if "IndexStatistics" in data:
        import aws_sdk_kendra.types.index_statistics

        out["index_statistics"] = (
            aws_sdk_kendra.types.index_statistics.deserialize_aws_json_1_1(
                data["IndexStatistics"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "CapacityUnits" in data:
        import aws_sdk_kendra.types.capacity_units_configuration

        out["capacity_units"] = (
            aws_sdk_kendra.types.capacity_units_configuration.deserialize_aws_json_1_1(
                data["CapacityUnits"]
            )
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
