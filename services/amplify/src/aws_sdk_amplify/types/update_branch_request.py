"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateBranchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.backend
    import aws_sdk_amplify.types.backend_environment_arn
    import aws_sdk_amplify.types.basic_auth_credentials
    import aws_sdk_amplify.types.branch_name
    import aws_sdk_amplify.types.build_spec
    import aws_sdk_amplify.types.compute_role_arn
    import aws_sdk_amplify.types.description
    import aws_sdk_amplify.types.display_name
    import aws_sdk_amplify.types.enable_auto_build
    import aws_sdk_amplify.types.enable_basic_auth
    import aws_sdk_amplify.types.enable_notification
    import aws_sdk_amplify.types.enable_performance_mode
    import aws_sdk_amplify.types.enable_pull_request_preview
    import aws_sdk_amplify.types.enable_skew_protection
    import aws_sdk_amplify.types.environment_variables
    import aws_sdk_amplify.types.framework
    import aws_sdk_amplify.types.pull_request_environment_name
    import aws_sdk_amplify.types.stage
    import aws_sdk_amplify.types.ttl


class UpdateBranchRequest(TypedDict):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p> The unique ID for an Amplify app. </p>"""
    branch_name: "aws_sdk_amplify.types.branch_name.BranchName"
    """<p>The name of the branch. </p>"""
    description: NotRequired["aws_sdk_amplify.types.description.Description"]
    """<p> The description for the branch. </p>"""
    framework: NotRequired["aws_sdk_amplify.types.framework.Framework"]
    """<p> The framework for the branch. </p>"""
    stage: NotRequired["aws_sdk_amplify.types.stage.Stage"]
    """<p> Describes the current stage for the branch. </p>"""
    enable_notification: NotRequired[
        "aws_sdk_amplify.types.enable_notification.EnableNotification"
    ]
    """<p> Enables notifications for the branch. </p>"""
    enable_auto_build: NotRequired[
        "aws_sdk_amplify.types.enable_auto_build.EnableAutoBuild"
    ]
    """<p> Enables auto building for the branch. </p>"""
    enable_skew_protection: NotRequired[
        "aws_sdk_amplify.types.enable_skew_protection.EnableSkewProtection"
    ]
    r"""<p>Specifies whether the skew protection feature is enabled for the branch.</p> <p>Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html\">Skew protection for Amplify deployments</a> in the <i>Amplify User Guide</i>.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_amplify.types.environment_variables.EnvironmentVariables"
    ]
    """<p> The environment variables for the branch. </p>"""
    basic_auth_credentials: NotRequired[
        "aws_sdk_amplify.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p> The basic authorization credentials for the branch. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>"""
    enable_basic_auth: NotRequired[
        "aws_sdk_amplify.types.enable_basic_auth.EnableBasicAuth"
    ]
    """<p> Enables basic authorization for the branch. </p>"""
    enable_performance_mode: NotRequired[
        "aws_sdk_amplify.types.enable_performance_mode.EnablePerformanceMode"
    ]
    """<p>Enables performance mode for the branch.</p> <p>Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out. </p>"""
    build_spec: NotRequired["aws_sdk_amplify.types.build_spec.BuildSpec"]
    """<p> The build specification (build spec) for the branch. </p>"""
    ttl: NotRequired["aws_sdk_amplify.types.ttl.TTL"]
    """<p> The content Time to Live (TTL) for the website in seconds. </p>"""
    display_name: NotRequired["aws_sdk_amplify.types.display_name.DisplayName"]
    """<p> The display name for a branch. This is used as the default domain prefix. </p>"""
    enable_pull_request_preview: NotRequired[
        "aws_sdk_amplify.types.enable_pull_request_preview.EnablePullRequestPreview"
    ]
    """<p> Enables pull request previews for this branch. </p>"""
    pull_request_environment_name: NotRequired[
        "aws_sdk_amplify.types.pull_request_environment_name.PullRequestEnvironmentName"
    ]
    """<p> The Amplify environment name for the pull request. </p>"""
    backend_environment_arn: NotRequired[
        "aws_sdk_amplify.types.backend_environment_arn.BackendEnvironmentArn"
    ]
    """<p>The Amazon Resource Name (ARN) for a backend environment that is part of a Gen 1 Amplify app. </p> <p>This field is available to Amplify Gen 1 apps only where the backend is created using Amplify Studio or the Amplify command line interface (CLI).</p>"""
    backend: NotRequired["aws_sdk_amplify.types.backend.Backend"]
    """<p>The backend for a <code>Branch</code> of an Amplify app. Use for a backend created from an CloudFormation stack.</p> <p>This field is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.</p>"""
    compute_role_arn: NotRequired[
        "aws_sdk_amplify.types.compute_role_arn.ComputeRoleArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the IAM role to assign to a branch of an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html\">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBranchRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "framework" in value:
        out["framework"] = value["framework"]
    if "stage" in value:
        import aws_sdk_amplify.types.stage

        out["stage"] = aws_sdk_amplify.types.stage.serialize_json(value["stage"])
    if "enable_notification" in value:
        out["enableNotification"] = value["enable_notification"]
    if "enable_auto_build" in value:
        out["enableAutoBuild"] = value["enable_auto_build"]
    if "enable_skew_protection" in value:
        out["enableSkewProtection"] = value["enable_skew_protection"]
    if "environment_variables" in value:
        import aws_sdk_amplify.types.environment_variables

        out["environmentVariables"] = (
            aws_sdk_amplify.types.environment_variables.serialize_json(
                value["environment_variables"]
            )
        )
    if "basic_auth_credentials" in value:
        out["basicAuthCredentials"] = value["basic_auth_credentials"]
    if "enable_basic_auth" in value:
        out["enableBasicAuth"] = value["enable_basic_auth"]
    if "enable_performance_mode" in value:
        out["enablePerformanceMode"] = value["enable_performance_mode"]
    if "build_spec" in value:
        out["buildSpec"] = value["build_spec"]
    if "ttl" in value:
        out["ttl"] = value["ttl"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "enable_pull_request_preview" in value:
        out["enablePullRequestPreview"] = value["enable_pull_request_preview"]
    if "pull_request_environment_name" in value:
        out["pullRequestEnvironmentName"] = value["pull_request_environment_name"]
    if "backend_environment_arn" in value:
        out["backendEnvironmentArn"] = value["backend_environment_arn"]
    if "backend" in value:
        import aws_sdk_amplify.types.backend

        out["backend"] = aws_sdk_amplify.types.backend.serialize_json(value["backend"])
    if "compute_role_arn" in value:
        out["computeRoleArn"] = value["compute_role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateBranchRequest:
    out: UpdateBranchRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "framework" in data:
        out["framework"] = data["framework"]
    if "stage" in data:
        import aws_sdk_amplify.types.stage

        out["stage"] = aws_sdk_amplify.types.stage.deserialize_json(data["stage"])
    if "enableNotification" in data:
        out["enable_notification"] = data["enableNotification"]
    if "enableAutoBuild" in data:
        out["enable_auto_build"] = data["enableAutoBuild"]
    if "enableSkewProtection" in data:
        out["enable_skew_protection"] = data["enableSkewProtection"]
    if "environmentVariables" in data:
        import aws_sdk_amplify.types.environment_variables

        out["environment_variables"] = (
            aws_sdk_amplify.types.environment_variables.deserialize_json(
                data["environmentVariables"]
            )
        )
    if "basicAuthCredentials" in data:
        out["basic_auth_credentials"] = data["basicAuthCredentials"]
    if "enableBasicAuth" in data:
        out["enable_basic_auth"] = data["enableBasicAuth"]
    if "enablePerformanceMode" in data:
        out["enable_performance_mode"] = data["enablePerformanceMode"]
    if "buildSpec" in data:
        out["build_spec"] = data["buildSpec"]
    if "ttl" in data:
        out["ttl"] = data["ttl"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "enablePullRequestPreview" in data:
        out["enable_pull_request_preview"] = data["enablePullRequestPreview"]
    if "pullRequestEnvironmentName" in data:
        out["pull_request_environment_name"] = data["pullRequestEnvironmentName"]
    if "backendEnvironmentArn" in data:
        out["backend_environment_arn"] = data["backendEnvironmentArn"]
    if "backend" in data:
        import aws_sdk_amplify.types.backend

        out["backend"] = aws_sdk_amplify.types.backend.deserialize_json(data["backend"])
    if "computeRoleArn" in data:
        out["compute_role_arn"] = data["computeRoleArn"]
    return out
