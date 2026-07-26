"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GroupType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.description_type
    import capo_cognito_identity_provider.types.group_name_type
    import capo_cognito_identity_provider.types.precedence_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class GroupType(TypedDict, closed=True):
    group_name: NotRequired[
        "capo_cognito_identity_provider.types.group_name_type.GroupNameType"
    ]
    """<p>The name of the group.</p>"""
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that contains the group.</p>"""
    description: NotRequired[
        "capo_cognito_identity_provider.types.description_type.DescriptionType"
    ]
    """<p>A friendly description of the group.</p>"""
    role_arn: NotRequired["capo_cognito_identity_provider.types.arn_type.ArnType"]
    """<p>The ARN of the IAM role associated with the group. If a group has the highest priority of a user's groups, users who authenticate with an identity pool get credentials for the <code>RoleArn</code> that's associated with the group.</p>"""
    precedence: NotRequired[
        "capo_cognito_identity_provider.types.precedence_type.PrecedenceType"
    ]
    """<p>A non-negative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. Zero is the highest precedence value. Groups with lower <code>Precedence</code> values take precedence over groups with higher ornull <code>Precedence</code> values. If a user belongs to two or more groups, it is the group with the lowest precedence value whose role ARN is given in the user's tokens for the <code>cognito:roles</code> and <code>cognito:preferred_role</code> claims.</p> <p>Two groups can have the same <code>Precedence</code> value. If this happens, neither group takes precedence over the other. If two groups with the same <code>Precedence</code> have the same role ARN, that role is used in the <code>cognito:preferred_role</code> claim in tokens for users in each group. If the two groups have different role ARNs, the <code>cognito:preferred_role</code> claim isn't set in users' tokens.</p> <p>The default <code>Precedence</code> value is <code>null</code>.</p>"""
    last_modified_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    creation_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupType) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "precedence" in value:
        out["Precedence"] = value["precedence"]
    if "last_modified_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["LastModifiedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CreationDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupType:
    out: GroupType = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Precedence" in data:
        out["precedence"] = data["Precedence"]
    if "LastModifiedDate" in data:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    if "CreationDate" in data:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    return out
