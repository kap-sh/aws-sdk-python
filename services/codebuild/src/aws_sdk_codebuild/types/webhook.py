"""Generated from Smithy shape ``com.amazonaws.codebuild#Webhook``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.filter_groups
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.pull_request_build_policy
    import aws_sdk_codebuild.types.scope_configuration
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.timestamp
    import aws_sdk_codebuild.types.webhook_build_type
    import aws_sdk_codebuild.types.webhook_status
    import aws_sdk_codebuild.types.wrapper_boolean


class Webhook(TypedDict):
    url: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The URL to the webhook.</p>"""
    payload_url: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The CodeBuild endpoint where webhook events are sent.</p>"""
    secret: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The secret token of the associated repository. </p> <note> <p>A Bitbucket webhook does not support <code>secret</code>. </p> </note>"""
    branch_filter: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If <code>branchFilter</code> is empty, then all branches are built.</p> <note> <p>It is recommended that you use <code>filterGroups</code> instead of <code>branchFilter</code>. </p> </note>"""
    filter_groups: NotRequired["aws_sdk_codebuild.types.filter_groups.FilterGroups"]
    """<p>An array of arrays of <code>WebhookFilter</code> objects used to determine which webhooks are triggered. At least one <code>WebhookFilter</code> in the array must specify <code>EVENT</code> as its <code>type</code>. </p> <p>For a build to be triggered, at least one filter group in the <code>filterGroups</code> array must pass. For a filter group to pass, each of its filters must pass. </p>"""
    build_type: NotRequired[
        "aws_sdk_codebuild.types.webhook_build_type.WebhookBuildType"
    ]
    r"""<p>Specifies the type of build this webhook will trigger.</p> <note> <p> <code>RUNNER_BUILDKITE_BUILD</code> is only available for <code>NO_SOURCE</code> source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html\">Tutorial: Configure a CodeBuild-hosted Buildkite runner</a> in the <i>CodeBuild user guide</i>.</p> </note>"""
    manual_creation: NotRequired[
        "aws_sdk_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p>If manualCreation is true, CodeBuild doesn't create a webhook in GitHub and instead returns <code>payloadUrl</code> and <code>secret</code> values for the webhook. The <code>payloadUrl</code> and <code>secret</code> values in the output can be used to manually create a webhook within GitHub.</p> <note> <p>manualCreation is only available for GitHub webhooks.</p> </note>"""
    last_modified_secret: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates the last time a repository's secret token was modified. </p>"""
    scope_configuration: NotRequired[
        "aws_sdk_codebuild.types.scope_configuration.ScopeConfiguration"
    ]
    """<p>The scope configuration for global or organization webhooks.</p> <note> <p>Global or organization webhooks are only available for GitHub and Github Enterprise webhooks.</p> </note>"""
    status: NotRequired["aws_sdk_codebuild.types.webhook_status.WebhookStatus"]
    """<p>The status of the webhook. Valid values include:</p> <ul> <li> <p> <code>CREATING</code>: The webhook is being created.</p> </li> <li> <p> <code>CREATE_FAILED</code>: The webhook has failed to create.</p> </li> <li> <p> <code>ACTIVE</code>: The webhook has succeeded and is active.</p> </li> <li> <p> <code>DELETING</code>: The webhook is being deleted.</p> </li> </ul>"""
    status_message: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>A message associated with the status of a webhook.</p>"""
    pull_request_build_policy: NotRequired[
        "aws_sdk_codebuild.types.pull_request_build_policy.PullRequestBuildPolicy"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Webhook) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    if "payload_url" in value:
        out["payloadUrl"] = value["payload_url"]
    if "secret" in value:
        out["secret"] = value["secret"]
    if "branch_filter" in value:
        out["branchFilter"] = value["branch_filter"]
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
    if "manual_creation" in value:
        out["manualCreation"] = value["manual_creation"]
    if "last_modified_secret" in value:
        import aws_sdk_codebuild.types.timestamp

        out["lastModifiedSecret"] = (
            aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_secret"]
            )
        )
    if "scope_configuration" in value:
        import aws_sdk_codebuild.types.scope_configuration

        out["scopeConfiguration"] = (
            aws_sdk_codebuild.types.scope_configuration.serialize_aws_json_1_1(
                value["scope_configuration"]
            )
        )
    if "status" in value:
        import aws_sdk_codebuild.types.webhook_status

        out["status"] = aws_sdk_codebuild.types.webhook_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "pull_request_build_policy" in value:
        import aws_sdk_codebuild.types.pull_request_build_policy

        out["pullRequestBuildPolicy"] = (
            aws_sdk_codebuild.types.pull_request_build_policy.serialize_aws_json_1_1(
                value["pull_request_build_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Webhook:
    out: Webhook = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    if "payloadUrl" in data:
        out["payload_url"] = data["payloadUrl"]
    if "secret" in data:
        out["secret"] = data["secret"]
    if "branchFilter" in data:
        out["branch_filter"] = data["branchFilter"]
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
    if "manualCreation" in data:
        out["manual_creation"] = data["manualCreation"]
    if "lastModifiedSecret" in data:
        import aws_sdk_codebuild.types.timestamp

        out["last_modified_secret"] = (
            aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
                data["lastModifiedSecret"]
            )
        )
    if "scopeConfiguration" in data:
        import aws_sdk_codebuild.types.scope_configuration

        out["scope_configuration"] = (
            aws_sdk_codebuild.types.scope_configuration.deserialize_aws_json_1_1(
                data["scopeConfiguration"]
            )
        )
    if "status" in data:
        import aws_sdk_codebuild.types.webhook_status

        out["status"] = aws_sdk_codebuild.types.webhook_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "pullRequestBuildPolicy" in data:
        import aws_sdk_codebuild.types.pull_request_build_policy

        out["pull_request_build_policy"] = (
            aws_sdk_codebuild.types.pull_request_build_policy.deserialize_aws_json_1_1(
                data["pullRequestBuildPolicy"]
            )
        )
    return out
