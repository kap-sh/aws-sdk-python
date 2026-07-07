"""Generated from Smithy shape ``com.amazonaws.amplify#AutoBranchCreationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.basic_auth_credentials
    import aws_sdk_amplify.types.build_spec
    import aws_sdk_amplify.types.enable_auto_build
    import aws_sdk_amplify.types.enable_basic_auth
    import aws_sdk_amplify.types.enable_performance_mode
    import aws_sdk_amplify.types.enable_pull_request_preview
    import aws_sdk_amplify.types.environment_variables
    import aws_sdk_amplify.types.framework
    import aws_sdk_amplify.types.pull_request_environment_name
    import aws_sdk_amplify.types.stage


class AutoBranchCreationConfig(TypedDict, closed=True):
    stage: NotRequired["aws_sdk_amplify.types.stage.Stage"]
    """<p>Describes the current stage for the autocreated branch. </p>"""
    framework: NotRequired["aws_sdk_amplify.types.framework.Framework"]
    """<p>The framework for the autocreated branch. </p>"""
    enable_auto_build: NotRequired[
        "aws_sdk_amplify.types.enable_auto_build.EnableAutoBuild"
    ]
    """<p>Enables auto building for the autocreated branch. </p>"""
    environment_variables: NotRequired[
        "aws_sdk_amplify.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables for the autocreated branch. </p>"""
    basic_auth_credentials: NotRequired[
        "aws_sdk_amplify.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p>The basic authorization credentials for the autocreated branch. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>"""
    enable_basic_auth: NotRequired[
        "aws_sdk_amplify.types.enable_basic_auth.EnableBasicAuth"
    ]
    """<p>Enables basic authorization for the autocreated branch. </p>"""
    enable_performance_mode: NotRequired[
        "aws_sdk_amplify.types.enable_performance_mode.EnablePerformanceMode"
    ]
    """<p>Enables performance mode for the branch.</p> <p>Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out. </p>"""
    build_spec: NotRequired["aws_sdk_amplify.types.build_spec.BuildSpec"]
    """<p>The build specification (build spec) for the autocreated branch. </p>"""
    enable_pull_request_preview: NotRequired[
        "aws_sdk_amplify.types.enable_pull_request_preview.EnablePullRequestPreview"
    ]
    """<p>Enables pull request previews for the autocreated branch. </p>"""
    pull_request_environment_name: NotRequired[
        "aws_sdk_amplify.types.pull_request_environment_name.PullRequestEnvironmentName"
    ]
    """<p>The Amplify environment name for the pull request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoBranchCreationConfig) -> dict:
    out: dict = {}
    if "stage" in value:
        import aws_sdk_amplify.types.stage

        out["stage"] = aws_sdk_amplify.types.stage.serialize_json(value["stage"])
    if "framework" in value:
        out["framework"] = value["framework"]
    if "enable_auto_build" in value:
        out["enableAutoBuild"] = value["enable_auto_build"]
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
    if "enable_pull_request_preview" in value:
        out["enablePullRequestPreview"] = value["enable_pull_request_preview"]
    if "pull_request_environment_name" in value:
        out["pullRequestEnvironmentName"] = value["pull_request_environment_name"]
    return out


def deserialize_json(data: dict) -> AutoBranchCreationConfig:
    out: AutoBranchCreationConfig = {}  # type: ignore[typeddict-item]
    if "stage" in data:
        import aws_sdk_amplify.types.stage

        out["stage"] = aws_sdk_amplify.types.stage.deserialize_json(data["stage"])
    if "framework" in data:
        out["framework"] = data["framework"]
    if "enableAutoBuild" in data:
        out["enable_auto_build"] = data["enableAutoBuild"]
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
    if "enablePullRequestPreview" in data:
        out["enable_pull_request_preview"] = data["enablePullRequestPreview"]
    if "pullRequestEnvironmentName" in data:
        out["pull_request_environment_name"] = data["pullRequestEnvironmentName"]
    return out
