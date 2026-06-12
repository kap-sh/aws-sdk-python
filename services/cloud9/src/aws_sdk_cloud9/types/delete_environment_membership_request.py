"""Generated from Smithy shape ``com.amazonaws.cloud9#DeleteEnvironmentMembershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloud9.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_id
    import aws_sdk_cloud9.types.user_arn


class DeleteEnvironmentMembershipRequest(TypedDict):
    environment_id: "aws_sdk_cloud9.types.environment_id.EnvironmentId"
    """<p>The ID of the environment to delete the environment member from.</p>"""
    user_arn: "aws_sdk_cloud9.types.user_arn.UserArn"
    """<p>The Amazon Resource Name (ARN) of the environment member to delete from the environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEnvironmentMembershipRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    out["userArn"] = value["user_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEnvironmentMembershipRequest:
    out: DeleteEnvironmentMembershipRequest = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "DeleteEnvironmentMembershipRequest.environment_id required"
        )
    if "userArn" in data:
        out["user_arn"] = data["userArn"]
    else:
        raise DeserializationError(
            "DeleteEnvironmentMembershipRequest.user_arn required"
        )
    return out
