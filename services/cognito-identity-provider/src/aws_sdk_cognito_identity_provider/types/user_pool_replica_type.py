"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolReplicaType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.arn_type
    import aws_sdk_cognito_identity_provider.types.region_name_type
    import aws_sdk_cognito_identity_provider.types.replica_role_type
    import aws_sdk_cognito_identity_provider.types.replica_status_type


class UserPoolReplicaType(TypedDict, closed=True):
    region_name: NotRequired[
        "aws_sdk_cognito_identity_provider.types.region_name_type.RegionNameType"
    ]
    """<p>The Amazon Web Services Region where the replica is located.</p>"""
    status: NotRequired[
        "aws_sdk_cognito_identity_provider.types.replica_status_type.ReplicaStatusType"
    ]
    """<p>The current status of the replica.</p> <dl> <dt>CREATING</dt> <dd> <p>The replica is being created.</p> </dd> <dt>INACTIVE</dt> <dd> <p>The replica has been created, but is not accepting requests for end-users. Administrator configuration operations are supported.</p> </dd> <dt>ACTIVE</dt> <dd> <p>The replica is available for both end-user and administrator operations.</p> </dd> <dt>DELETING</dt> <dd> <p>The replica is being deleted.</p> </dd> </dl>"""
    role: NotRequired[
        "aws_sdk_cognito_identity_provider.types.replica_role_type.ReplicaRoleType"
    ]
    """<p>The role of the user pool replica that determines which API operations are enabled.</p> <dl> <dt>PRIMARY</dt> <dd> <p>The primary replica supports all end user and administrator operations.</p> </dd> <dt>SECONDARY</dt> <dd> <p>The secondary replica supports a limited set of end user and administrator operations. Generally, only administrator operations that set configurations specific to the replica, and only end-user operations that do not create or change attributes of a user are supported. </p> </dd> </dl>"""
    user_pool_arn: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The Amazon Resource Name (ARN) of the replica user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolReplicaType) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "status" in value:
        import aws_sdk_cognito_identity_provider.types.replica_status_type

        out["Status"] = (
            aws_sdk_cognito_identity_provider.types.replica_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "role" in value:
        import aws_sdk_cognito_identity_provider.types.replica_role_type

        out["Role"] = (
            aws_sdk_cognito_identity_provider.types.replica_role_type.serialize_aws_json_1_1(
                value["role"]
            )
        )
    if "user_pool_arn" in value:
        out["UserPoolArn"] = value["user_pool_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolReplicaType:
    out: UserPoolReplicaType = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    if "Status" in data:
        import aws_sdk_cognito_identity_provider.types.replica_status_type

        out["status"] = (
            aws_sdk_cognito_identity_provider.types.replica_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Role" in data:
        import aws_sdk_cognito_identity_provider.types.replica_role_type

        out["role"] = (
            aws_sdk_cognito_identity_provider.types.replica_role_type.deserialize_aws_json_1_1(
                data["Role"]
            )
        )
    if "UserPoolArn" in data:
        out["user_pool_arn"] = data["UserPoolArn"]
    return out
