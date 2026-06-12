"""Generated from Smithy shape ``com.amazonaws.codebuild#PullRequestBuildApproverRoles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.pull_request_build_approver_role

PullRequestBuildApproverRoles: TypeAlias = list[
    "aws_sdk_codebuild.types.pull_request_build_approver_role.PullRequestBuildApproverRole"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestBuildApproverRoles) -> list:
    import aws_sdk_codebuild.types.pull_request_build_approver_role

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.pull_request_build_approver_role.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PullRequestBuildApproverRoles:
    import aws_sdk_codebuild.types.pull_request_build_approver_role

    out: PullRequestBuildApproverRoles = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.pull_request_build_approver_role.deserialize_aws_json_1_1(
                item
            )
        )
    return out
