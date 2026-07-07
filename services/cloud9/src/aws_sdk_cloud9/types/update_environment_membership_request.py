"""Generated from Smithy shape ``com.amazonaws.cloud9#UpdateEnvironmentMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloud9.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_id
    import aws_sdk_cloud9.types.member_permissions
    import aws_sdk_cloud9.types.user_arn


class UpdateEnvironmentMembershipRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_cloud9.types.environment_id.EnvironmentId"
    """<p>The ID of the environment for the environment member whose settings you want to change.</p>"""
    user_arn: "aws_sdk_cloud9.types.user_arn.UserArn"
    """<p>The Amazon Resource Name (ARN) of the environment member whose settings you want to change.</p>"""
    permissions: "aws_sdk_cloud9.types.member_permissions.MemberPermissions"
    """<p>The replacement type of environment member permissions you want to associate with this environment member. Available values include:</p> <ul> <li> <p> <code>read-only</code>: Has read-only access to the environment.</p> </li> <li> <p> <code>read-write</code>: Has read-write access to the environment.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEnvironmentMembershipRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    out["userArn"] = value["user_arn"]
    import aws_sdk_cloud9.types.member_permissions

    out["permissions"] = aws_sdk_cloud9.types.member_permissions.serialize_aws_json_1_1(
        value["permissions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEnvironmentMembershipRequest:
    out: UpdateEnvironmentMembershipRequest = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "UpdateEnvironmentMembershipRequest.environment_id required"
        )
    if "userArn" in data:
        out["user_arn"] = data["userArn"]
    else:
        raise DeserializationError(
            "UpdateEnvironmentMembershipRequest.user_arn required"
        )
    if "permissions" in data:
        import aws_sdk_cloud9.types.member_permissions

        out["permissions"] = (
            aws_sdk_cloud9.types.member_permissions.deserialize_aws_json_1_1(
                data["permissions"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEnvironmentMembershipRequest.permissions required"
        )
    return out
