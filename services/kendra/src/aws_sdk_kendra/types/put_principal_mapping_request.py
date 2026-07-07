"""Generated from Smithy shape ``com.amazonaws.kendra#PutPrincipalMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_id
    import aws_sdk_kendra.types.group_id
    import aws_sdk_kendra.types.group_members
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.principal_ordering_id
    import aws_sdk_kendra.types.role_arn


class PutPrincipalMappingRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to map users to their groups.</p>"""
    data_source_id: NotRequired["aws_sdk_kendra.types.data_source_id.DataSourceId"]
    r"""<p>The identifier of the data source you want to map users to their groups.</p> <p>This is useful if a group is tied to multiple data sources, but you only want the group to access documents of a certain data source. For example, the groups \"Research\", \"Engineering\", and \"Sales and Marketing\" are all tied to the company's documents stored in the data sources Confluence and Salesforce. However, \"Sales and Marketing\" team only needs access to customer-related documents stored in Salesforce.</p>"""
    group_id: "aws_sdk_kendra.types.group_id.GroupId"
    """<p>The identifier of the group you want to map its users to.</p>"""
    group_members: "aws_sdk_kendra.types.group_members.GroupMembers"
    r"""<p>The list that contains your users that belong the same group. This can include sub groups that belong to a group.</p> <p>For example, the group \"Company A\" includes the user \"CEO\" and the sub groups \"Research\", \"Engineering\", and \"Sales and Marketing\".</p> <p>If you have more than 1000 users and/or sub groups for a single group, you need to provide the path to the S3 file that lists your users and sub groups for a group. Your sub groups can contain more than 1000 users, but the list of sub groups that belong to a group (and/or users) must be no more than 1000.</p>"""
    ordering_id: NotRequired[
        "aws_sdk_kendra.types.principal_ordering_id.PrincipalOrderingId"
    ]
    """<p>The timestamp identifier you specify to ensure Amazon Kendra doesn't override the latest <code>PUT</code> action with previous actions. The highest number ID, which is the ordering ID, is the latest action you want to process and apply on top of other actions with lower number IDs. This prevents previous actions with lower number IDs from possibly overriding the latest action.</p> <p>The ordering ID can be the Unix time of the last update you made to a group members list. You would then provide this list when calling <code>PutPrincipalMapping</code>. This ensures your <code>PUT</code> action for that updated group with the latest members list doesn't get overwritten by earlier <code>PUT</code> actions for the same group which are yet to be processed.</p> <p>The default ordering ID is the current Unix time in milliseconds that the action was received by Amazon Kendra.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that has access to the S3 file that contains your list of users that belong to a group.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html#iam-roles-ds\">IAM roles for Amazon Kendra</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPrincipalMappingRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    out["GroupId"] = value["group_id"]
    import aws_sdk_kendra.types.group_members

    out["GroupMembers"] = aws_sdk_kendra.types.group_members.serialize_aws_json_1_1(
        value["group_members"]
    )
    if "ordering_id" in value:
        out["OrderingId"] = value["ordering_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPrincipalMappingRequest:
    out: PutPrincipalMappingRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("PutPrincipalMappingRequest.index_id required")
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("PutPrincipalMappingRequest.group_id required")
    if "GroupMembers" in data:
        import aws_sdk_kendra.types.group_members

        out["group_members"] = (
            aws_sdk_kendra.types.group_members.deserialize_aws_json_1_1(
                data["GroupMembers"]
            )
        )
    else:
        raise DeserializationError("PutPrincipalMappingRequest.group_members required")
    if "OrderingId" in data:
        out["ordering_id"] = data["OrderingId"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
