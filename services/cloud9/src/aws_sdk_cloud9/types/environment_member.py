"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloud9.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_id
    import aws_sdk_cloud9.types.permissions
    import aws_sdk_cloud9.types.string
    import aws_sdk_cloud9.types.timestamp
    import aws_sdk_cloud9.types.user_arn


class EnvironmentMember(TypedDict, closed=True):
    permissions: "aws_sdk_cloud9.types.permissions.Permissions"
    """<p>The type of environment member permissions associated with this environment member. Available values include:</p> <ul> <li> <p> <code>owner</code>: Owns the environment.</p> </li> <li> <p> <code>read-only</code>: Has read-only access to the environment.</p> </li> <li> <p> <code>read-write</code>: Has read-write access to the environment.</p> </li> </ul>"""
    user_id: "aws_sdk_cloud9.types.string.String"
    """<p>The user ID in Identity and Access Management (IAM) of the environment member.</p>"""
    user_arn: "aws_sdk_cloud9.types.user_arn.UserArn"
    """<p>The Amazon Resource Name (ARN) of the environment member.</p>"""
    environment_id: "aws_sdk_cloud9.types.environment_id.EnvironmentId"
    """<p>The ID of the environment for the environment member.</p>"""
    last_access: NotRequired["aws_sdk_cloud9.types.timestamp.Timestamp"]
    """<p>The time, expressed in epoch time format, when the environment member last opened the environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentMember) -> dict:
    out: dict = {}
    import aws_sdk_cloud9.types.permissions

    out["permissions"] = aws_sdk_cloud9.types.permissions.serialize_aws_json_1_1(
        value["permissions"]
    )
    out["userId"] = value["user_id"]
    out["userArn"] = value["user_arn"]
    out["environmentId"] = value["environment_id"]
    if "last_access" in value:
        import aws_sdk_cloud9.types.timestamp

        out["lastAccess"] = aws_sdk_cloud9.types.timestamp.serialize_aws_json_1_1(
            value["last_access"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentMember:
    out: EnvironmentMember = {}  # type: ignore[typeddict-item]
    if "permissions" in data:
        import aws_sdk_cloud9.types.permissions

        out["permissions"] = aws_sdk_cloud9.types.permissions.deserialize_aws_json_1_1(
            data["permissions"]
        )
    else:
        raise DeserializationError("EnvironmentMember.permissions required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("EnvironmentMember.user_id required")
    if "userArn" in data:
        out["user_arn"] = data["userArn"]
    else:
        raise DeserializationError("EnvironmentMember.user_arn required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("EnvironmentMember.environment_id required")
    if "lastAccess" in data:
        import aws_sdk_cloud9.types.timestamp

        out["last_access"] = aws_sdk_cloud9.types.timestamp.deserialize_aws_json_1_1(
            data["lastAccess"]
        )
    return out
