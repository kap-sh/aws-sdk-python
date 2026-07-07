"""Generated from Smithy shape ``com.amazonaws.cloud9#DescribeEnvironmentMembershipsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_members_list
    import aws_sdk_cloud9.types.string


class DescribeEnvironmentMembershipsResult(TypedDict, closed=True):
    memberships: NotRequired[
        "aws_sdk_cloud9.types.environment_members_list.EnvironmentMembersList"
    ]
    """<p>Information about the environment members for the environment.</p>"""
    next_token: NotRequired["aws_sdk_cloud9.types.string.String"]
    """<p>If there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a <i>next token</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEnvironmentMembershipsResult) -> dict:
    out: dict = {}
    if "memberships" in value:
        import aws_sdk_cloud9.types.environment_members_list

        out["memberships"] = (
            aws_sdk_cloud9.types.environment_members_list.serialize_aws_json_1_1(
                value["memberships"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEnvironmentMembershipsResult:
    out: DescribeEnvironmentMembershipsResult = {}  # type: ignore[typeddict-item]
    if "memberships" in data:
        import aws_sdk_cloud9.types.environment_members_list

        out["memberships"] = (
            aws_sdk_cloud9.types.environment_members_list.deserialize_aws_json_1_1(
                data["memberships"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
