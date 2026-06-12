"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateWebhookInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.boolean
    import aws_sdk_codebuild.types.filter_groups
    import aws_sdk_codebuild.types.project_name
    import aws_sdk_codebuild.types.pull_request_build_policy
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.webhook_build_type


class UpdateWebhookInput(TypedDict):
    project_name: "aws_sdk_codebuild.types.project_name.ProjectName"
    """<p>The name of the CodeBuild project.</p>"""
    branch_filter: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If <code>branchFilter</code> is empty, then all branches are built.</p> <note> <p> It is recommended that you use <code>filterGroups</code> instead of <code>branchFilter</code>. </p> </note>"""
    rotate_secret: "aws_sdk_codebuild.types.boolean.Boolean"
    """<p> A boolean value that specifies whether the associated GitHub repository's secret token should be updated. If you use Bitbucket for your repository, <code>rotateSecret</code> is ignored. </p>"""
    filter_groups: NotRequired["aws_sdk_codebuild.types.filter_groups.FilterGroups"]
    """<p> An array of arrays of <code>WebhookFilter</code> objects used to determine if a webhook event can trigger a build. A filter group must contain at least one <code>EVENT</code> <code>WebhookFilter</code>. </p>"""
    build_type: NotRequired[
        "aws_sdk_codebuild.types.webhook_build_type.WebhookBuildType"
    ]
    """<p>Specifies the type of build this webhook will trigger.</p> <note> <p> <code>RUNNER_BUILDKITE_BUILD</code> is only available for <code>NO_SOURCE</code> source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html\">Tutorial: Configure a CodeBuild-hosted Buildkite runner</a> in the <i>CodeBuild user guide</i>.</p> </note>"""
    pull_request_build_policy: NotRequired[
        "aws_sdk_codebuild.types.pull_request_build_policy.PullRequestBuildPolicy"
    ]
    """<p>A PullRequestBuildPolicy object that defines comment-based approval requirements for triggering builds on pull requests. This policy helps control when automated builds are executed based on contributor permissions and approval workflows.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebhookInput) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    if "branch_filter" in value:
        out["branchFilter"] = value["branch_filter"]
    out["rotateSecret"] = value.get("rotate_secret", False)
    if "filter_groups" in value:
        import aws_sdk_codebuild.types.filter_groups

        out["filterGroups"] = (
            aws_sdk_codebuild.types.filter_groups.serialize_aws_json_1_1(
                value["filter_groups"]
            )
        )
    if "build_type" in value:
        import aws_sdk_codebuild.types.webhook_build_type

        out["buildType"] = (
            aws_sdk_codebuild.types.webhook_build_type.serialize_aws_json_1_1(
                value["build_type"]
            )
        )
    if "pull_request_build_policy" in value:
        import aws_sdk_codebuild.types.pull_request_build_policy

        out["pullRequestBuildPolicy"] = (
            aws_sdk_codebuild.types.pull_request_build_policy.serialize_aws_json_1_1(
                value["pull_request_build_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWebhookInput:
    out: UpdateWebhookInput = {}  # type: ignore[typeddict-item]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("UpdateWebhookInput.project_name required")
    if "branchFilter" in data:
        out["branch_filter"] = data["branchFilter"]
    if "rotateSecret" in data:
        out["rotate_secret"] = data["rotateSecret"]
    else:
        out["rotate_secret"] = False
    if "filterGroups" in data:
        import aws_sdk_codebuild.types.filter_groups

        out["filter_groups"] = (
            aws_sdk_codebuild.types.filter_groups.deserialize_aws_json_1_1(
                data["filterGroups"]
            )
        )
    if "buildType" in data:
        import aws_sdk_codebuild.types.webhook_build_type

        out["build_type"] = (
            aws_sdk_codebuild.types.webhook_build_type.deserialize_aws_json_1_1(
                data["buildType"]
            )
        )
    if "pullRequestBuildPolicy" in data:
        import aws_sdk_codebuild.types.pull_request_build_policy

        out["pull_request_build_policy"] = (
            aws_sdk_codebuild.types.pull_request_build_policy.deserialize_aws_json_1_1(
                data["pullRequestBuildPolicy"]
            )
        )
    return out
