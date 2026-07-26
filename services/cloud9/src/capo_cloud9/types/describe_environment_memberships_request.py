"""Generated from Smithy shape ``com.amazonaws.cloud9#DescribeEnvironmentMembershipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_id
    import capo_cloud9.types.max_results
    import capo_cloud9.types.permissions_list
    import capo_cloud9.types.string
    import capo_cloud9.types.user_arn


class DescribeEnvironmentMembershipsRequest(TypedDict, closed=True):
    user_arn: NotRequired["capo_cloud9.types.user_arn.UserArn"]
    """<p>The Amazon Resource Name (ARN) of an individual environment member to get information about. If no value is specified, information about all environment members are returned.</p>"""
    environment_id: NotRequired["capo_cloud9.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment to get environment member information about.</p>"""
    permissions: NotRequired["capo_cloud9.types.permissions_list.PermissionsList"]
    """<p>The type of environment member permissions to get information about. Available values include:</p> <ul> <li> <p> <code>owner</code>: Owns the environment.</p> </li> <li> <p> <code>read-only</code>: Has read-only access to the environment.</p> </li> <li> <p> <code>read-write</code>: Has read-write access to the environment.</p> </li> </ul> <p>If no value is specified, information about all environment members are returned.</p>"""
    next_token: NotRequired["capo_cloud9.types.string.String"]
    """<p>During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a <i>next token</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>"""
    max_results: NotRequired["capo_cloud9.types.max_results.MaxResults"]
    """<p>The maximum number of environment members to get information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEnvironmentMembershipsRequest) -> dict:
    out: dict = {}
    if "user_arn" in value:
        out["userArn"] = value["user_arn"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "permissions" in value:
        import capo_cloud9.types.permissions_list

        out["permissions"] = capo_cloud9.types.permissions_list.serialize_aws_json_1_1(
            value["permissions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEnvironmentMembershipsRequest:
    out: DescribeEnvironmentMembershipsRequest = {}  # type: ignore[typeddict-item]
    if "userArn" in data:
        out["user_arn"] = data["userArn"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "permissions" in data:
        import capo_cloud9.types.permissions_list

        out["permissions"] = (
            capo_cloud9.types.permissions_list.deserialize_aws_json_1_1(
                data["permissions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
