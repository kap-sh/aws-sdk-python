"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.capacity_units_configuration
    import aws_sdk_kendra.types.description
    import aws_sdk_kendra.types.document_metadata_configuration_list
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.index_name
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.user_context_policy
    import aws_sdk_kendra.types.user_group_resolution_configuration
    import aws_sdk_kendra.types.user_token_configuration_list


class UpdateIndexRequest(TypedDict):
    id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to update.</p>"""
    name: NotRequired["aws_sdk_kendra.types.index_name.IndexName"]
    """<p>A new name for the index.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    """<p>An Identity and Access Management (IAM) role that gives Amazon Kendra permission to access Amazon CloudWatch logs and metrics.</p>"""
    description: NotRequired["aws_sdk_kendra.types.description.Description"]
    """<p>A new description for the index.</p>"""
    document_metadata_configuration_updates: NotRequired[
        "aws_sdk_kendra.types.document_metadata_configuration_list.DocumentMetadataConfigurationList"
    ]
    """<p>The document metadata configuration you want to update for the index. Document metadata are fields or attributes associated with your documents. For example, the company department name associated with each document.</p>"""
    capacity_units: NotRequired[
        "aws_sdk_kendra.types.capacity_units_configuration.CapacityUnitsConfiguration"
    ]
    """<p>Sets the number of additional document storage and query capacity units that should be used by the index. You can change the capacity of the index up to 5 times per day, or make 5 API calls.</p> <p>If you are using extra storage units, you can't reduce the storage capacity below what is required to meet the storage needs for your index.</p>"""
    user_token_configurations: NotRequired[
        "aws_sdk_kendra.types.user_token_configuration_list.UserTokenConfigurationList"
    ]
    """<p>The user token configuration.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>UserTokenConfigurations</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>"""
    user_context_policy: NotRequired[
        "aws_sdk_kendra.types.user_context_policy.UserContextPolicy"
    ]
    """<p>The user context policy.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can only use <code>ATTRIBUTE_FILTER</code> to filter search results by user context. If you're using an Amazon Kendra Gen AI Enterprise Edition index and you try to use <code>USER_TOKEN</code> to configure user context policy, Amazon Kendra returns a <code>ValidationException</code> error.</p> </important>"""
    user_group_resolution_configuration: NotRequired[
        "aws_sdk_kendra.types.user_group_resolution_configuration.UserGroupResolutionConfiguration"
    ]
    r"""<p>Gets users and groups from IAM Identity Center identity source. To configure this, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_UserGroupResolutionConfiguration.html\">UserGroupResolutionConfiguration</a>. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.</p> <important> <p>If you're using an Amazon Kendra Gen AI Enterprise Edition index, <code>UserGroupResolutionConfiguration</code> isn't supported.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIndexRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "document_metadata_configuration_updates" in value:
        import aws_sdk_kendra.types.document_metadata_configuration_list

        out["DocumentMetadataConfigurationUpdates"] = (
            aws_sdk_kendra.types.document_metadata_configuration_list.serialize_aws_json_1_1(
                value["document_metadata_configuration_updates"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> UpdateIndexRequest:
    out: UpdateIndexRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateIndexRequest.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DocumentMetadataConfigurationUpdates" in data:
        import aws_sdk_kendra.types.document_metadata_configuration_list

        out["document_metadata_configuration_updates"] = (
            aws_sdk_kendra.types.document_metadata_configuration_list.deserialize_aws_json_1_1(
                data["DocumentMetadataConfigurationUpdates"]
            )
        )
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
