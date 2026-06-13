"""Generated from Smithy shape ``com.amazonaws.quicksight#RedshiftIAMParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.database_group_list
    import aws_sdk_quicksight.types.database_user
    import aws_sdk_quicksight.types.role_arn


class RedshiftIAMParameters(TypedDict):
    role_arn: "aws_sdk_quicksight.types.role_arn.RoleArn"
    """<p>Use the <code>RoleArn</code> structure to allow Quick Sight to call <code>redshift:GetClusterCredentials</code> on your cluster. The calling principal must have <code>iam:PassRole</code> access to pass the role to Quick Sight. The role's trust policy must allow the Quick Sight service principal to assume the role.</p>"""
    database_user: NotRequired["aws_sdk_quicksight.types.database_user.DatabaseUser"]
    """<p>The user whose permissions and group memberships will be used by Quick Sight to access the cluster. If this user already exists in your database, Amazon Quick Sight is granted the same permissions that the user has. If the user doesn't exist, set the value of <code>AutoCreateDatabaseUser</code> to <code>True</code> to create a new user with PUBLIC permissions.</p>"""
    database_groups: NotRequired[
        "aws_sdk_quicksight.types.database_group_list.DatabaseGroupList"
    ]
    """<p>A list of groups whose permissions will be granted to Quick Sight to access the cluster. These permissions are combined with the permissions granted to Quick Sight by the <code>DatabaseUser</code>. If you choose to include this parameter, the <code>RoleArn</code> must grant access to <code>redshift:JoinGroup</code>.</p>"""
    auto_create_database_user: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>Automatically creates a database user. If your database doesn't have a <code>DatabaseUser</code>, set this parameter to <code>True</code>. If there is no <code>DatabaseUser</code>, Quick Sight can't connect to your cluster. The <code>RoleArn</code> that you use for this operation must grant access to <code>redshift:CreateClusterUser</code> to successfully create the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftIAMParameters) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    if "database_user" in value:
        out["DatabaseUser"] = value["database_user"]
    if "database_groups" in value:
        import aws_sdk_quicksight.types.database_group_list

        out["DatabaseGroups"] = (
            aws_sdk_quicksight.types.database_group_list.serialize_json(
                value["database_groups"]
            )
        )
    out["AutoCreateDatabaseUser"] = value.get("auto_create_database_user", False)
    return out


def deserialize_json(data: dict) -> RedshiftIAMParameters:
    out: RedshiftIAMParameters = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("RedshiftIAMParameters.role_arn required")
    if "DatabaseUser" in data:
        out["database_user"] = data["DatabaseUser"]
    if "DatabaseGroups" in data:
        import aws_sdk_quicksight.types.database_group_list

        out["database_groups"] = (
            aws_sdk_quicksight.types.database_group_list.deserialize_json(
                data["DatabaseGroups"]
            )
        )
    if "AutoCreateDatabaseUser" in data:
        out["auto_create_database_user"] = data["AutoCreateDatabaseUser"]
    else:
        out["auto_create_database_user"] = False
    return out
